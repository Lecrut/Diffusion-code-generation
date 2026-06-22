def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [3, 5.5, 0, -1]
    for value in sample_values:
        try:
            print(calculate_square_area(value))
        except ValueError as e:
            print(e)