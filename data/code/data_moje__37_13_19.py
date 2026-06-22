import math

def calculate_parallelogram_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return base * height

if __name__ == '__main__':
    base_value = 10.5
    height_value = 4.2
    area_result = calculate_parallelogram_area(base_value, height_value)
    print(area_result)