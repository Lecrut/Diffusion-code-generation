BOARD_SIZE = 8

def generate_checkerboard(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]
if __name__ == '__main__':
    result = generate_checkerboard(BOARD_SIZE)
    for row in result:
        print(row)