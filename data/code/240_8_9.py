def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 5.0
    area = calculate_square_area(sample_side)
    print(f"The area of a square with side length {sample_side} is {area}")