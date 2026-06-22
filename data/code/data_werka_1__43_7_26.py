def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = [4.0, 6.5, 8]
    for side in sample_side_lengths:
        area = calculate_square_area(side)
        print(area)