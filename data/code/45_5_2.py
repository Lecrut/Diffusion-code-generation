def circle_area_validator(func):
    def wrapper(*args, **kwargs):
        radius = args[0]
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return func(*args, **kwargs)
    return wrapper
@circle_area_validator
def calculate_circle_area(radius):
    return 3.14159 * radius**2
if __name__ == '__main__':
    try:
        print(calculate_circle_area(5))
        print(calculate_circle_area(0))
        print(calculate_circle_area(-2))
    except ValueError as e:
        print(f"Error: {e}")