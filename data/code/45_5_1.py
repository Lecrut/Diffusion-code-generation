def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return radius
class CircleAreaContext:
    def __init__(self, radius):
        self.radius = radius
    def __enter__(self):
        validated_radius = validate_radius(self.radius)
        return validated_radius
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
def calculate_circle_area(radius):
    validated_radius = validate_radius(radius)
    return 3.14159 * validated_radius ** 2
def area_decorator(func):
    def wrapper(*args):
        if len(args) == 1:
            radius = args[0]
            try:
                result = func(validate_radius(radius))
                return result
            except ValueError as e:
                raise e
        else:
            return func(*args)
    return wrapper
@area_decorator
def calculate_area_decorated(radius):
    return 3.14159 * radius ** 2
if __name__ == '__main__':
    sample_radius_valid = 5.0
    sample_radius_invalid = -2.0
    print(f"Testing valid radius {sample_radius_valid}: {calculate_area_decorated(sample_radius_valid)}")
    try:
        calculate_area_decorated(sample_radius_invalid)
    except ValueError as e:
        print(f"Caught expected error for invalid radius {sample_radius_invalid}: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")