def compute_square_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    side_value = 8
    calculated_area = compute_square_area(side_value)
    print(f"The area of a square with side {side_value} is: {calculated_area}")