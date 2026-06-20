def sort_coordinates(coords):
    return sorted(coords, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 1), (2, 4)]
    sorted_coords = sort_coordinates(sample_coords)
    print(sorted_coords)