def calculate_square_area(side):
    if not isinstance(side, (int, float)) or side < 0:
        raise ValueError("Side must be a non-negative number")
    return side * side

if __name__ == '__main__':
    sample_side = 4
    try:
        area = calculate_square_area(sample_side)
        print(f"Side: {sample_side}, Area: {area}")
    except ValueError as e:
        print(e)