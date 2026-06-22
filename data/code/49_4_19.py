SIZE = 4

def build_star_row():
    return '*' * SIZE

def create_star_square():
    return [build_star_row() for _ in range(SIZE)]

if __name__ == '__main__':
    square = create_star_square()
    print(len(square))
    print(square[0])
    print(len(square[0]))