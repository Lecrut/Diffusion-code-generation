import math

PI = 3.141592653589793

def validate_positive_number(value, name):
    try:
        converted = float(value)
        if converted <= 0:
            raise ValueError(f"{name} must be positive")
        return converted
    except TypeError:
        raise TypeError(f"{name} must be numeric")

def get_triangle_area(base, height):
    validated_base = validate_positive_number(base, "base")
    validated_height = validate_positive_number(height, "height")
    return validated_base * validated_height / 2

if __name__ == '__main__':
    demo_base = 8
    demo_height = 4
    computed_area = get_triangle_area(demo_base, demo_height)
    print(computed_area)