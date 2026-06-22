def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 7.8, -3, 0]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"Area: {area}")
        except ValueError as e:
            print(e)