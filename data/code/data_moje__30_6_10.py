def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric value")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    import math
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        result = calculate_circle_area(5)
        print(result)
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")