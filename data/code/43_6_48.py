def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [2, 6.8, -1, 0]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(area)
        except ValueError as e:
            print(e)