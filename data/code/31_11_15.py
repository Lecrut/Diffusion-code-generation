def get_square_area(side):
    if side < 0:
        return 0
    return side ** 2

if __name__ == '__main__':
    print(get_square_area(15))