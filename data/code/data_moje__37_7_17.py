import operator

def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def calculate_area(base, height):
    validated_base = validate_positive(base, "base")
    validated_height = validate_positive(height, "height")
    return operator.mul(validated_base, validated_height)

if __name__ == '__main__':
    BASE = 12
    HEIGHT = 6
    area = calculate_area(BASE, HEIGHT)
    print(area)