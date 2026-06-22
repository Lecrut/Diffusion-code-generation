def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    triangle_sides = {
        'side1': 3.5,
        'side2': 4.2,
        'side3': 5.1
    }
    perimeter = calculate_perimeter(triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3'])
    print(perimeter)