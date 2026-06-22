def calculate_square_area(side):
    try:
        side = float(side)
        if side < 0:
            raise ValueError("Side cannot be negative")
        return side * side
    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        return None

if __name__ == '__main__':
    sample_side = 4
    area = calculate_square_area(sample_side)
    if area is not None:
        print(f"Side: {sample_side}, Area: {area}")