def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = [2, 4, 6]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of a square with side length {side} is {area}.")