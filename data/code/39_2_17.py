import math

def calculate_prism_volume(base_area: float, height: float) -> float:
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    volume = calculate_prism_volume(base, height)
    print(volume)