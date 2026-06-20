def custom_sort(coordinates):
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    sorted_coords = custom_sort(sample_coords)
    print(sorted_coords)