def sort_coordinates(coordinates):
    if not all(isinstance(coord, tuple) and len(coord) == 2 and isinstance(x, (int, float)) and isinstance(y, (int, float)) for coord in coordinates for x, y in [coord]):
        raise ValueError("All elements must be tuples of two numeric values.")
    
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    print(sort_coordinates(sample_coords))