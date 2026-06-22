def square_area(side):
    if isinstance(side, int):
        return side * side
    return side ** 2

if __name__ == '__main__':
    side_length = 5
    area = square_area(side_length)
    print(area)