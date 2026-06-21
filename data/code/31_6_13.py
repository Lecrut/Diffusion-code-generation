def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [5, 10, 0, -3]
    for val in sample_values:
        try:
            area = calculate_square_area(val)
            print(f"Area for side {val}: {area}")
        except ValueError as e:
            print(f"Error for side {val}: {e}")