def validate_radius(func):
    def wrapper(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return func(radius)
    return wrapper

@validate_radius
def calculate_area(radius):
    return 3.14159 * radius * radius

if __name__ == '__main__':
    print(calculate_area(5))
    print(calculate_area(2.5))
    print(calculate_area(0.1))