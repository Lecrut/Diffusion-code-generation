def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be positive numbers")
    return a + b + c

if __name__ == '__main__':
    side1 = 7.5
    side2 = 9.3
    side3 = 4.8
    perimeter = calculate_perimeter(side1, side2, side3)
    print(perimeter)