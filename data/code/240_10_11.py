def calculate_square_area(side):
    area = side * side
    return area

if __name__ == '__main__':
    sample_side = 5
    area = calculate_square_area(sample_side)
    print(f"The area of the square with side length {sample_side} is: {area}")