def calculate_area_of_square(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_sides = [3, 4.5, 7, 0]
    for side in sample_sides:
        area = calculate_area_of_square(side)
        print(f"Side Length: {side}, Area: {area}")