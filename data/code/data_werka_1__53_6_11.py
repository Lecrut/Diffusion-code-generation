def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    SAMPLE_SIDES = [3, 5, 7, 10]
    for side in SAMPLE_SIDES:
        area = calculate_square_area(side)
        print(f"Side Length: {side}, Area: {area}")