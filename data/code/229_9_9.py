class SquareGrid:
    def __init__(self, N):
        self.N = N

    def get_perimeter(self):
        perimeter = set()
        for i in range(self.N):
            perimeter.add((i, 0))
            perimeter.add((i, self.N - 1))
        for j in range(1, self.N - 1):
            perimeter.add((0, j))
            perimeter.add((self.N - 1, j))
        return list(perimeter)

if __name__ == '__main__':
    grid = SquareGrid(10)
    perimeter_points = grid.get_perimeter()
    for point in perimeter_points:
        print(point)