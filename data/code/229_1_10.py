def generate_square_grid(N):
    return [[(i, j) for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    sample_size = 5
    result = generate_square_grid(sample_size)
    print(result)