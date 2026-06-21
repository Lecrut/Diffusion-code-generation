def compute_square_properties(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    side_length = area ** 0.5
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    areas = {'square1': 16, 'square2': 25}
    for name, area in areas.items():
        try:
            side_length, perimeter = compute_square_properties(area)
            print(f"Square {name}: Side Length: {side_length}, Perimeter: {perimeter}")
        except ValueError as e:
            print(e)