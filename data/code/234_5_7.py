import itertools

def create_checkerboard(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    checkerboard = create_checkerboard(8)
    print(checkerboard)