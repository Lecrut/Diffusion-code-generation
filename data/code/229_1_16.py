def generate_square_grid(N):
    return [[(i, j) for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    N_sample = 5
    result = generate_square_grid(N_sample)
    print(result)