def sort_coordinates(coordinates):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
        raise ValueError("All elements must be tuples of two numerical values.")
    
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    sorted_coords = sort_coordinates(sample_coords)
    print(sorted_coords)