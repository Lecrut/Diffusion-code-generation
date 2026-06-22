from typing import Final

BASE_AREA: Final[float] = 50.0
HEIGHT: Final[float] = 20.0

def calculate_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    volume = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(volume)