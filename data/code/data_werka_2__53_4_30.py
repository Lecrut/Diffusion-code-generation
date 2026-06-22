def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be positive")
    return side * side

if __name__ == '__main__':
    sample_sides = [4, 6, 8]
    for side in sample_sides:
        try:
            print(f"The area of the square with side {side} is: {calculate_square_area(side)}")
        except ValueError as e:
            print(e)