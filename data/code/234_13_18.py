def create_checkerboard(size):
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    sample_size = 10
    checkerboard = create_checkerboard(sample_size)
    print(checkerboard)