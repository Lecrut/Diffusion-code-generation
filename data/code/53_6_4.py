def calculate_area_of_square(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 7, 10.5]
    for side in sample_sides:
        try:
            area = calculate_area_of_square(side)
            print(f"Side Length: {side}, Area: {area}")
        except ValueError as e:
            print(e)