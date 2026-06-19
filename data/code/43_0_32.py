SQUARE_AREA_FACTOR = 2

def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 10]
    for side_length in sample_sides:
        area = calculate_square_area(side_length)
        print(f"The area of a square with side length {side_length} is {area}.")