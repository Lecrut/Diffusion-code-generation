class CoordinateSorter:
    @staticmethod
    def sort_coordinates(coordinates):
        return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

if __name__ == '__main__':
    sample_coords = [(3, 2), (1, 5), (3, 4), (1, 1)]
    sorter = CoordinateSorter()
    sorted_coords = sorter.sort_coordinates(sample_coords)
    print(sorted_coords)