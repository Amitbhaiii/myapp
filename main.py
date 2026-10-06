import pygame
import math
import time

pygame.init()

# =========================================================
# FUTURISTIC CYBER SECURITY HUD - V4.0 (ULTRA SLEEK)
# Pydroid 3 / Pygame Responsive Fullscreen
# =========================================================

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_size()

pygame.display.set_caption("CYBER SECURITY // V4.0")
clock = pygame.time.Clock()

# ---------------------------------------------------------
# PALETTE (Vibrant Cyber Cyan & Deep Obsidian)
# ---------------------------------------------------------

BG = (1, 5, 6)
PANEL_BG = (3, 15, 16, 220)
BORDER_CYAN = (0, 230, 210)
DIM_CYAN = (0, 90, 85)
NEON_GREEN = (0, 255, 120)
TEXT_WHITE = (225, 255, 250)
GRID_COLOR = (2, 22, 21)

# ---------------------------------------------------------
# SCALING SETUP (Base 1000x1500 Layout Engine)
# ---------------------------------------------------------

BASE_W = 1000
BASE_H = 1500

SX = W / BASE_W
SY = H / BASE_H
S = min(SX, SY)

def X(v): return int(v * SX)
def Y(v): return int(v * SY)
def FS(v): return max(9, int(v * S))

# ---------------------------------------------------------
# FONTS
# ---------------------------------------------------------

def get_font(size, bold=False):
    return pygame.font.SysFont("monospace", FS(size), bold=bold)

F_TINY = get_font(14)
F_SMALL = get_font(18)
F_MED = get_font(23, True)
F_BIG = get_font(50, True)
F_SCORE = get_font(95, True)

# ---------------------------------------------------------
# DRAWING HELPERS
# ---------------------------------------------------------

def draw_rect(x, y, w, h, color, width=0):
    pygame.draw.rect(screen, color, (X(x), Y(y), X(w), Y(h)), width=max(1, X(width)) if width else 0)

def draw_line(x1, y1, x2, y2, color, width=1):
    pygame.draw.line(screen, color, (X(x1), Y(y1)), (X(x2), Y(y2)), max(1, X(width)))

def draw_corner(x, y, fx, fy, size=28, color=BORDER_CYAN):
    draw_line(x, y, x + size * fx, y, color, 2)
    draw_line(x, y, x, y + size * fy, color, 2)

def draw_text(msg, x, y, font_obj, color=TEXT_WHITE, center=False):
    surf = font_obj.render(msg, True, color)
    rect = surf.get_rect(center=(X(x), Y(y))) if center else surf.get_rect(topleft=(X(x), Y(y)))
    screen.blit(surf, rect)

# ---------------------------------------------------------
# BACKGROUND TECHNICAL GRID
# ---------------------------------------------------------

def draw_cyber_grid():
    # Dense tech grid lines
    for x in range(0, BASE_W + 1, 40):
        draw_line(x, 0, x, BASE_H, GRID_COLOR, 1)
    for y in range(0, BASE_H + 1, 40):
        draw_line(0, y, BASE_W, y, GRID_COLOR, 1)

# ---------------------------------------------------------
# TOP HUD BAR
# ---------------------------------------------------------

def draw_top_bar():
    x, y, w, h = 45, 45, 910, 70
    draw_rect(x, y, w, h, (2, 12, 14))
    draw_rect(x, y, w, h, DIM_CYAN, 1)
    
    # Title Tag
    draw_rect(x + 12, y + 12, 600, 46, BORDER_CYAN)
    draw_text("[ CYBER SECURITY // HUD V4.0 ]", x + 25, y + 23, F_MED, BG)
    
    # Live Status Box
    draw_rect(x + 630, y + 12, 268, 46, (1, 25, 23))
    draw_text("● SYSTEM ONLINE", x + 650, y + 26, F_SMALL, NEON_GREEN)
    
    draw_corner(x, y, 1, 1, 20)
    draw_corner(x + w, y, -1, 1, 20)
    draw_corner(x, y + h, 1, -1, 20)
    draw_corner(x + w, y + h, -1, -1, 20)

# ---------------------------------------------------------
# CENTRAL RADAR PANEL (SCORE)
# ---------------------------------------------------------

def draw_radar_panel():
    cx, cy = 290, 350
    x, y, w, h = 45, 135, 445, 430
    
    draw_rect(x, y, w, h, (2, 10, 11))
    draw_rect(x, y, w, h, DIM_CYAN, 1)
    
    # Header strip
    draw_text("SECURITY INDEX // RADAR SCAN", x + 20, y + 15, F_TINY, BORDER_CYAN)
    
    # Concentric Radar Rings
    for r in [160, 120, 80, 40]:
        pygame.draw.circle(screen, DIM_CYAN, (X(cx), Y(cy)), X(r), max(1, X(1)))
        
    # Crosshairs
    draw_line(cx - 170, cy, cx + 170, cy, DIM_CYAN, 1)
    draw_line(cx, cy - 170, cx, cy + 170, DIM_CYAN, 1)
    
    # Rotating Beam
    angle = time.time() * 2.5
    rx = cx + math.cos(angle) * 160
    ry = cy + math.sin(angle) * 160
    draw_line(cx, cy, rx, ry, NEON_GREEN, 2)
    
    # Center Score & Status
    draw_text("100", cx, cy - 22, F_SCORE, TEXT_WHITE, center=True)
    draw_text("SECURE SYSTEM", cx, cy + 48, F_SMALL, NEON_GREEN, center=True)
    
    draw_corner(x, y, 1, 1)
    draw_corner(x + w, y, -1, 1)
    draw_corner(x, y + h, 1, -1)
    draw_corner(x + w, y + h, -1, -1)

# ---------------------------------------------------------
# SYSTEM ANALYSIS PANEL (RIGHT)
# ---------------------------------------------------------

def draw_analysis_panel():
    x, y, w, h = 510, 135, 445, 430
    draw_rect(x, y, w, h, (2, 10, 11))
    draw_rect(x, y, w, h, DIM_CYAN, 1)
    
    draw_text("BIOMETRIC & THREAT SIGNATURE", x + 20, y + 15, F_TINY, BORDER_CYAN)
    
    # Fingerprint / Neural core graphic simulation
    nx, ny = 732, 350
    for r in range(30, 140, 22):
        pygame.draw.ellipse(screen, DIM_CYAN, (X(nx - r*0.7), Y(ny - r), X(r*1.4), Y(r*2)), X(1))
        
    draw_text("STATUS: ENCRYPTED", x + 20, y + 385, F_TINY, NEON_GREEN)
    
    draw_corner(x, y, 1, 1)
    draw_corner(x + w, y, -1, 1)
    draw_corner(x, y + h, 1, -1)
    draw_corner(x + w, y + h, -1, -1)

# ---------------------------------------------------------
# OPTIMIZE BUTTON
# ---------------------------------------------------------

def draw_optimize_button(is_active):
    x, y, w, h = 45, 585, 910, 85
    
    btn_color = (0, 45, 42) if is_active else (2, 15, 17)
    draw_rect(x, y, w, h, btn_color)
    draw_rect(x, y, w, h, BORDER_CYAN if is_active else DIM_CYAN, 2)
    
    # Animated laser sweep inside button
    sweep_x = x + int((time.time() * 300) % w)
    draw_line(sweep_x, y + 5, sweep_x, y + h - 5, NEON_GREEN, 2)
    
    if is_active:
        draw_text("[ EXECUTING SYSTEM DEEP PURGE... ]", x + w/2, y + 25, F_MED, BORDER_CYAN, center=True)
        draw_text("FLUSHING CACHE // CLEARING SOCKETS // SECURING PORTS", x + w/2, y + 58, F_TINY, NEON_GREEN, center=True)
    else:
        draw_text("[ OPTIMIZE SYSTEM CORE ]", x + w/2, y + 28, F_MED, BORDER_CYAN, center=True)
        draw_text("TAP TO INITIATE FULL SECURITY OPTIMIZATION", x + w/2, y + 58, F_TINY, TEXT_WHITE, center=True)
        
    draw_corner(x, y, 1, 1, 20)
    draw_corner(x + w, y, -1, 1, 20)
    draw_corner(x, y + h, 1, -1, 20)
    draw_corner(x + w, y + h, -1, -1, 20)

# ---------------------------------------------------------
# SECURITY MODULE CARDS
# ---------------------------------------------------------

def draw_security_card(x, y, w, h, code, title, status):
    draw_rect(x, y, w, h, (2, 12, 13))
    draw_rect(x, y, w, h, DIM_CYAN, 1)
    
    # Code tag & Title
    draw_text(code, x + 18, y + 16, F_TINY, BORDER_CYAN)
    draw_text(title, x + 18, y + 42, F_SMALL, TEXT_WHITE)
    draw_text("● " + status, x + 18, y + 78, F_TINY, NEON_GREEN)
    
    # Mini Progress Bar
    bar_w = w - 36
    draw_rect(x + 18, y + 105, bar_w, 4, DIM_CYAN)
    active_bar = int(((math.sin(time.time() * 3 + x) + 1) / 2) * bar_w)
    draw_rect(x + 18, y + 105, active_bar, 4, BORDER_CYAN)
    
    draw_corner(x, y, 1, 1, 15)
    draw_corner(x + w, y + h, -1, -1, 15)

def draw_all_cards():
    y1, y2, y3 = 695, 845, 995
    cw, ch = 445, 130
    
    # Row 1
    draw_security_card(45, y1, cw, ch, "[SYS_01]", "PHISHING SHIELD", "ACTIVE LINK WATCHDOG")
    draw_security_card(510, y1, cw, ch, "[NET_02]", "DATA LEAK AUDIT", "NETWORK SOCKETS CLEAN")
    
    # Row 2
    draw_security_card(45, y2, cw, ch, "[OPT_03]", "CAMERA DETECTOR", "OPTICAL SCAN READY")
    draw_security_card(510, y2, cw, ch, "[LOG_04]", "THREAT LOG VAULT", "0 RISKY SIGNATURES")
    
    # Row 3 (Wide Card)
    draw_security_card(45, y3, 910, ch, "[APP_05]", "APP CLEANUP & STORAGE ENGINE", "FREE STORAGE READY // OPTIMIZED")

# ---------------------------------------------------------
# LOWER TELEMETRY & SCANLINE
# ---------------------------------------------------------

def draw_telemetry_bar():
    y = 1150
    draw_line(45, y, 955, y, DIM_CYAN, 1)
    
    draw_text("SYS://SECURE", 55, y + 15, F_TINY, DIM_CYAN)
    draw_text("NET://LISTENING", 380, y + 15, F_TINY, DIM_CYAN)
    draw_text("ENCRYPTION: AES-256", 720, y + 15, F_TINY, NEON_GREEN)

    # Activity frequency bars
    for i in range(22):
        lvl = int((math.sin(time.time() * 4 + i) + 1) * 9)
        draw_rect(55 + i * 39, y + 45, 28, lvl + 4, DIM_CYAN)

def draw_global_scanline():
    scan_y = int((time.time() * 60) % BASE_H)
    draw_line(0, scan_y, BASE_W, scan_y, (0, 45, 40), 1)

# ---------------------------------------------------------
# MAIN EXECUTION LOOP
# ---------------------------------------------------------

is_optimizing = False
opt_timer = 0
running = True

while running:
    now = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Check Optimize Button Click
            if X(45) <= mx <= X(955) and Y(585) <= my <= Y(670):
                is_optimizing = True
                opt_timer = now + 2.0

    if is_optimizing and now >= opt_timer:
        is_optimizing = False

    # Render Frame
    screen.fill(BG)
    
    draw_cyber_grid()
    draw_top_bar()
    draw_radar_panel()
    draw_analysis_panel()
    draw_optimize_button(is_optimizing)
    draw_all_cards()
    draw_telemetry_bar()
    draw_global_scanline()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
  
