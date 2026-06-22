def calculate_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        sides = [7, 15, 23]
        perimeter = calculate_perimeter(*sides)
        print(perimeter)
    except ValueError as e:
        print(e)