def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [4, 9.5, 12]
    for value in sample_values:
        print(calculate_square_area(value))