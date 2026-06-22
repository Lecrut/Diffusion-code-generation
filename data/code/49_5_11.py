def print_square_pattern(n):
    rows = [["*" for _ in range(n)] for _ in range(n)]
    for row in rows:
        print("".join(row))

if __name__ == '__main__':
    dimension = 8
    print_square_pattern(dimension)