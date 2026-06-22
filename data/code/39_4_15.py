from __future__ import annotations

BASE_AREA_MULTIPLIER = 1.0

def calculate_prism_volume(base_area: float, height: float) -> float:
    return base_area * height * BASE_AREA_MULTIPLIER

if __name__ == '__main__':
    base = 12.0
    h = 7.0
    volume = calculate_prism_volume(base, h)
    print(volume)