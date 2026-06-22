def generate_square_grid(N):
    if N <= 0:
        return []

    perimeter = set()

    for i in range(N):
        perimeter.add((i, 0))
        perimeter.add((N-1, i))
        perimeter.add((i, N-1))
        perimeter.add((0, i))

    return list(perimeter)

if __name__ == '__main__':
    N_sample = 10
    result_grid = generate_square_grid(N_sample)
    print(result_grid)