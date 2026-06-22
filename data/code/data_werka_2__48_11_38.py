def calculate_square_properties(area):
    side_length = area ** 0.5
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    square_areas = {'small': 16, 'medium': 25}
    for size, area in square_areas.items():
        side_length, perimeter = calculate_square_properties(area)
        print(f"{size.capitalize()} Square - Side Length: {side_length}, Perimeter: {perimeter}")