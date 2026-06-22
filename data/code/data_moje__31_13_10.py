def square_area(side):
    if side < 0:
        return 0
    return side ** 2

if __name__ == '__main__':
    side_length = 20
    area = square_area(side_length)
    print(area)