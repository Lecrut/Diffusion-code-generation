def generate_grid():
    return [[(i, j) for j in range(5)] for i in range(5)]

if __name__ == '__main__':
    print(generate_grid())