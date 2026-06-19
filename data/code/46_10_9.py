def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return None
    return a + b + c

if __name__ == '__main__':
    sides = {
        'side1': 7.5,
        'side2': 9.5,
        'side3': 6.5
    }
    
    perimeter = calculate_triangle_perimeter(sides['side1'], sides['side2'], sides['side3'])
    if perimeter is not None:
        print(perimeter)