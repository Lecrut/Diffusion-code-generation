def calculate_perimeter(length, width):
    if not all(isinstance(d, (int, float)) and d > 0 for d in [length, width]):
        raise ValueError("Both length and width must be positive numbers.")
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        result = calculate_perimeter(10, 5)
        print(f"Perimeter: {result}")
    except ValueError as e:
        print(e)