def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 6
    area_result = calculate_square_area(sample_side_length)
    print(f"The area of a square with side length {sample_side_length} is {area_result}")