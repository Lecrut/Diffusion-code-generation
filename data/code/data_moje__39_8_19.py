import math

def calculate_prism_volume(base_area, height):
    if base_area < 0:
        raise ValueError("Base area cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return base_area * height

if __name__ == '__main__':
    base_area = 25.5
    height = 10.0
    volume = calculate_prism_volume(base_area, height)
    print(volume)