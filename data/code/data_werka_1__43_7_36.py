def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [4, 6, 8]
    for length in sample_side_lengths:
        area = calculate_square_area(length)
        print(area)