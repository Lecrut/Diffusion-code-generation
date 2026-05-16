def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be positive.")
    return side * side
if __name__ == '__main__':
    try:
        result1 = calculate_square_area(5)
        print(f"Area of a square with side 5: {result1}")
        result2 = calculate_square_area(10.5)
        print(f"Area of a square with side 10.5: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        calculate_square_area(0)
    except ValueError as e:
        print(f"Error caught for zero input: {e}")
    try:
        calculate_square_area(-3)
    except ValueError as e:
        print(f"Error caught for negative input: {e}")