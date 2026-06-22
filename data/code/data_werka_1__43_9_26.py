def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    example_side = 7
    calculated_area = calculate_square_area(example_side)
    print(f"The area of a square with side length {example_side} is {calculated_area}")