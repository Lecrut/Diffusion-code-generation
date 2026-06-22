import math

def calculate_perimeter(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both parameters must be numbers")
    
    return 2 * math.pi * math.sqrt(0.5 * ((a**2 + b**2) + abs(a**2 - b**2)))

if __name__ == '__main__':
    a1, b1 = 3, 4
    perimeter1 = calculate_perimeter(a1, b1)
    print(f"Perimeter for ellipse with semi-major axis {a1} and semi-minor axis {b1}: {perimeter1}")
    
    a2, b2 = 10, 20
    perimeter2 = calculate_perimeter(a2, b2)
    print(f"Perimeter for ellipse with semi-major axis {a2} and semi-minor axis {b2}: {perimeter2}")