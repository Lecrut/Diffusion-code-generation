def generate_square_grid():
    return {
        (i, j): False for i in range(3) for j in range(3)
    }

if __name__ == '__main__':
    sample_grid = generate_square_grid()
    print(sample_grid)