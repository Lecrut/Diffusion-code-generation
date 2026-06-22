import math

def validate_positive_number(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a numeric value")
    if math.isnan(value) or math.isinf(value):
        raise ValueError(f"{name} cannot be NaN or infinite")
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return value

def triangle_area(base, height):
    validated_base = validate_positive_number(base, "Base")
    validated_height = validate_positive_number(height, "Height")
    return 0.5 * validated_base * validated_height

if __name__ == '__main__':
    result_1 = triangle_area(20, 15)
    print(result_1)
    result_2 = triangle_area(3.5, 2.2)
    print(result_2)
    try:
        triangle_area(0, 10)
    except ValueError as e:
        print(e)
    try:
        triangle_area(10, -5)
    except ValueError as e:
        print(e)
    try:
        triangle_area("10", 5)
    except TypeError as e:
        print(e)