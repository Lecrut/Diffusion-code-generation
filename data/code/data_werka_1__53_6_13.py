def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_sides = [2, 4, 6, 8]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"Side Length: {side}, Area: {area}")