def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    SAMPLE_SIDES = [3, 5, 7]
    for side in SAMPLE_SIDES:
        area = calculate_square_area(side)
        print(area)