def calculate_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 10
        side2 = 5
        side3 = 7
        result = calculate_perimeter(side1, side2, side3)
        print(f"Perimeter for sides {side1}, {side2}, and {side3}: {result}")
    except ValueError as e:
        print(f"Error: {e}")