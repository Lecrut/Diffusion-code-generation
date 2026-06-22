import math
RAMANUJAN_FACTOR = 1 + 3 * math.sqrt(2) / (10 * math.pi)

def calculate_perimeter(a, b):
    return RAMANUJAN_FACTOR * (a + b) * math.sqrt((4 * a * b + (a - b) ** 2) / (4 * a * b))
if __name__ == '__main__':
    a1, b1 = (3, 4)
    perimeter1 = calculate_perimeter(a1, b1)
    print(f'Perimeter for ellipse with semi-major axis {a1} and semi-minor axis {b1}: {perimeter1:.2f}')
    a2, b2 = (10, 20)
    perimeter2 = calculate_perimeter(a2, b2)
    print(f'Perimeter for ellipse with semi-major axis {a2} and semi-minor axis {b2}: {perimeter2:.2f}')
    a3, b3 = (1, 1)
    perimeter3 = calculate_perimeter(a3, b3)
    print(f'Perimeter for ellipse with semi-major axis {a3} and semi-minor axis {b3}: {perimeter3:.2f}')