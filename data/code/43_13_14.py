def calculate_square_area(side_length):
    if side_length <= 0:
        return None
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = [2, 3, 5]
    for side in sample_side_lengths:
        area = calculate_square_area(side)
        if area is not None:
            print(f"The area of the square with side length {side} is: {area}")