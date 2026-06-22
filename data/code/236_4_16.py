import itertools

class TriangleRepeater:
    @staticmethod
    def get_triangle_coordinates():
        return [(0, 0), (1, 2), (3, 4)]

    @staticmethod
    def repeat_and_print(coordinates, count):
        repeated_coords = list(itertools.chain.from_iterable(itertools.repeat(coordinates, count)))
        for coord in repeated_coords:
            print(f"{coord[0]}, {coord[1]}")

if __name__ == '__main__':
    sample_triangle = TriangleRepeater.get_triangle_coordinates()
    TriangleRepeater.repeat_and_print(sample_triangle, 3)