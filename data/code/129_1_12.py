def sort_coordinates(coordinates):
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(2, 3), (4, 1), (2, 5), (4, 2)]
    sorted_coords = sort_coordinates(sample_coords)
    for coord in sorted_coords:
        print(coord)