def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = [3, 5.5, 7]
    for length in sample_side_lengths:
        area = calculate_square_area(length)
        print(f"The area of a square with side length {length} is {area}.")