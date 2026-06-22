def print_star_square():
    dimension = 8
    row = ["*"] * dimension
    for i in range(dimension):
        print("".join(row))

if __name__ == '__main__':
    print_star_square()