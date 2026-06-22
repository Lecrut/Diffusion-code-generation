import numpy as np

def generate_square_grid(n):
    return np.fromfunction(lambda i, j: (i + j) % 2, (n, n))

if __name__ == '__main__':
    sample_size = 5
    result = generate_square_grid(sample_size)
    print(result)