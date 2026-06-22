SQUARE_AREA_MULTIPLIER = 1

def calculate_square_area(side_length):
    return side_length * SQUARE_AREA_MULTIPLIER * side_length

if __name__ == '__main__':
    sample_values = [4.5, 6.7, 9.3]
    for value in sample_values:
        print(calculate_square_area(value))