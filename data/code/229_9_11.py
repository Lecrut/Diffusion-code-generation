import itertools
GRID_SIZE = 10

def generate_square_perimeter(N):
    all_points = set(itertools.product(range(N), range(N)))
    top_edge = {(0, j) for j in range(N)}
    bottom_edge = {(N - 1, j) for j in range(N)}
    left_edge = {(i, 0) for i in range(1, N - 1)}
    right_edge = {(i, N - 1) for i in range(1, N - 1)}
    perimeter_points = top_edge.union(bottom_edge).union(left_edge).union(right_edge)
    return list(perimeter_points)
if __name__ == '__main__':
    sample_perimeter = generate_square_perimeter(GRID_SIZE)
    print(sample_perimeter)