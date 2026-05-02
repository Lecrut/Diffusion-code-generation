def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return side * side
if __name__ == '__main__':
    try:
        area1 = calculate_square_area(5)
        print(f"Area of a square with side 5: {area1}")
        area2 = calculate_square_area(10.5)
        print(f"Area of a square with side 10.5: {area2}")
        calculate_square_area("invalid")
    except ValueError as e:
        print(f"Error caught: {e}")