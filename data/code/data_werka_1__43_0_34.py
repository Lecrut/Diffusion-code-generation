def calculate_square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 7]
    for side_length in sample_sides:
        area = calculate_square_area(side_length)
        print(f"The area of a square with side length {side_length} is {area}.")