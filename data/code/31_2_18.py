def square_area(side):
    if isinstance(side, int) and side >= 0:
        return side << side if side != 1 else side * side
    return side ** 2

if __name__ == '__main__':
    result = square_area(5)
    print(result)