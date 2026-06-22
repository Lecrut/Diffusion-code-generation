import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area

def calculate_side_length(area):
    validated_area = validate_area(area)
    return math.sqrt(validated_area)

if __name__ == '__main__':
    area_value = 25.0
    side_length = calculate_side_length(area_value)
    print(f"The side length of the square is: {side_length}")