def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    SAMPLE_VALUES = [4, 6, 9.3]
    for value in SAMPLE_VALUES:
        print(calculate_square_area(value))