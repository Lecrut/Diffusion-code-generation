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
        area1 = calculate_circle_area(5)
        print(f"Area for radius 5: {area1}")
        area2 = calculate_circle_area(10.5)
        print(f"Area for radius 10.5: {area2}")
        try:
            calculate_circle_area(-2)
        except ValueError as e:
            print(f"Caught expected error for radius -2: {e}")
        try:
            calculate_circle_area(0)
        except ValueError as e:
            print(f"Caught expected error for radius 0: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")