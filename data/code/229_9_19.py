class GridGenerator:
    N = 10

    @staticmethod
    def get_perimeter_points(N):
        perimeter = set()
        for i in range(N):
            perimeter.add((i, 0))
            perimeter.add((i, N-1))
        for j in range(1, N-1):
            perimeter.add((0, j))
            perimeter.add((N-1, j))
        return list(perimeter)

if __name__ == '__main__':
    perimeter_points = GridGenerator.get_perimeter_points(GridGenerator.N)
    print(perimeter_points)