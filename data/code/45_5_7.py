def circle_area_validator(func):
    def wrapper(*args, **kwargs):
        radius = args[0]
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return func(*args, **kwargs)
    return wrapper
@circle_area_validator
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
if __name__ == '__main__':
    try:
        area1 = calculate_circle_area(5)
        print(f"Area for radius 5: {area1}")
        area2 = calculate_circle_area(0)
        print(f"Area for radius 0: {area2}")
        area3 = calculate_circle_area(-2)
        print(f"Area for radius -2: {area3}")
    except ValueError as e:
        print(f"Error caught: {e}")