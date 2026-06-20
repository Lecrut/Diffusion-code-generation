def validate_coordinates(coordinates):
    if not all(isinstance(coord, tuple) and len(coord) == 2 and isinstance(x, (int, float)) and isinstance(y, (int, float))
                for coord in coordinates for x, y in [coord]):
        raise ValueError("Invalid coordinate format. Each element must be a tuple of two numbers.")

def sort_coordinates(coordinates):
    validate_coordinates(coordinates)
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    sorted_coords = sort_coordinates(sample_coords)
    print(sorted_coords)