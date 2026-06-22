def generate_checkerboard(size):
    return [[(i + j) % 2 for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    checkerboard = generate_checkerboard(10)
    for row in checkerboard:
        print(row)