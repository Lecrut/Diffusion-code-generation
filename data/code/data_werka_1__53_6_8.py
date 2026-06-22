def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = [2, 4, 6, 8]
    for i, side_length in enumerate(sample_sides, start=1):
        area = calculate_square_area(side_length)
        print(f"Sample {i}: Side Length = {side_length}, Area = {area}")