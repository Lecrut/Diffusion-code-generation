def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return side * side
if __name__ == '__main__':
    try:
        result1 = calculate_square_area(5)
        print(f"Area of square with side 5: {result1}")
        result2 = calculate_square_area(10.5)
        print(f"Area of square with side 10.5: {result2}")
        calculate_square_area("a")
    except ValueError as e:
        print(f"Error caught: {e}")