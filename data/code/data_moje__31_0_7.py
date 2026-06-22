def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be a number")
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return side ** 2

if __name__ == '__main__':
    sample_sides = [0, 5, 10.5, -3]
    for s in sample_sides:
        try:
            area = calculate_square_area(s)
            print(f"Area for side {s}: {area}")
        except Exception as e:
            print(f"Error for side {s}: {e}")