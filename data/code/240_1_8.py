def calculate_square_area(side: int) -> int:
    return side * side

if __name__ == '__main__':
    sample_side = 5
    area = calculate_square_area(sample_side)
    print(f"The area of a square with side {sample_side} is: {area}")