import math

AREA_UNIT_MAP = {"circle": "square units"}

def get_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius_value = 3
    result = get_area(radius_value)
    print(result)