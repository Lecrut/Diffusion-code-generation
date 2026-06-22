def calculate_square_area(side: int) -> int:
    return side * side

if __name__ == '__main__':
    sample_sides = [5, 10, 3]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of a square with side {side} is: {area}")