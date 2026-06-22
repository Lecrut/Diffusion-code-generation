import math

CIRCLE_CONSTANT = math.pi

def compute_circle_area(radius: float) -> float:
    return CIRCLE_CONSTANT * radius * radius

if __name__ == '__main__':
    radius_value = 10
    area_result = compute_circle_area(radius_value)
    print(area_result)