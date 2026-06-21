import math

def calculate_circle_area(radius):
    try:
        radius = float(radius)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius
    except (TypeError, ValueError) as e:
        return str(e)

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(0))
    print(calculate_circle_area(-3))
    print(calculate_circle_area("abc"))
    print(calculate_circle_area([1, 2, 3]))