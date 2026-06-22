def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a numeric type")
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

if __name__ == '__main__':
    sample_sides = [5, 0, 3.5, -2]
    for s in sample_sides:
        try:
            area = calculate_square_area(s)
            print(f"Area for side {s}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error for side {s}: {e}")