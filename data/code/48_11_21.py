def compute_square_properties(area):
    side_length = area ** 0.5
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    area_values = {'square1': 16, 'square2': 25}
    for name, area in area_values.items():
        side_length, perimeter = compute_square_properties(area)
        print(f"Square {name}: Side Length: {side_length}, Perimeter: {perimeter}")