def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [3, 5, 10]
    for value in sample_values:
        print(calculate_square_area(value))