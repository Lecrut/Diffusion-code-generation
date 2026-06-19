def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = [4, 6, 8]
    for side_length in sample_sides:
        area = calculate_square_area(side_length)
        print(f"The area of a square with side length {side_length} is {area}.")