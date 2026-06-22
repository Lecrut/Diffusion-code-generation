import math

CONE_CONSTANT = 1 / 3

def calculate_cone_volume(radius: float, height: float) -> float:
    squared_radius = radius * radius
    base_area = math.pi * squared_radius
    total_volume = base_area * height * CONE_CONSTANT
    return total_volume

if __name__ == '__main__':
    test_radius = 8.0
    test_height = 15.0
    computed_result = calculate_cone_volume(test_radius, test_height)
    print(computed_result)