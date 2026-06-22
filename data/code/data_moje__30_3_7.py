def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 3.141592653589793 * radius ** 2

if __name__ == '__main__':
    result = calculate_circle_area(5)
    print(result)