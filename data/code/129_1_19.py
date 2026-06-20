def validate_coordinates(coordinates):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
        raise ValueError("All items must be numerical tuples of length 2")

def sort_coordinates(coordinates):
    validate_coordinates(coordinates)
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    print(sort_coordinates(sample_coords))