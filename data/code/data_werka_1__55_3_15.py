def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    sides = {
        'side1': 3.5,
        'side2': 4.5,
        'side3': 5.5
    }
    
    perimeter = calculate_perimeter(sides['side1'], sides['side2'], sides['side3'])
    print(perimeter)