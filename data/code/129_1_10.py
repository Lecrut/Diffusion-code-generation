def sort_coordinates(coords):
    return sorted(coords, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(4, 3), (2, 5), (4, 6), (2, 2)]
    sorted_coords = sort_coordinates(sample_coords)
    print(sorted_coords)