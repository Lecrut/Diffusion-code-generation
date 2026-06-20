def sort_coordinates(coordinates):
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 1), (2, 4)]
    print(sort_coordinates(sample_coords))