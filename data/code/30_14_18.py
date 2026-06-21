import math

def validate_radius(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Radius must be a number")
    if value < 0:
        raise ValueError("Radius cannot be negative")
    return float(value)

def compute_circle_area(radius):
    validated_radius = validate_radius(radius)
    squared_radius = validated_radius * validated_radius
    area_value = math.pi * squared_radius
    return area_value

def format_area_output(area):
    return area

if __name__ == "__main__":
    test_radius_value = 7.25
    try:
        calculated_area = compute_circle_area(test_radius_value)
        print(calculated_area)
    except (ValueError, TypeError) as error:
        print(f"Calculation failed: {error}")