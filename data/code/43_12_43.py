def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [4, 6, 9]
    for index, length in enumerate(sample_side_lengths, start=1):
        area_result = calculate_square_area(length)
        print(f"Sample {index}: The area of a square with side length {length} is {area_result}")