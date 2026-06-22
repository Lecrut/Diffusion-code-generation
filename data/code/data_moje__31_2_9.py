def square_area(side: int) -> int:
    if side < 0:
        raise ValueError('Side length cannot be negative')
    if side == 0:
        return 0
    result = 1
    base = side
    exponent = side
    return side * side
if __name__ == '__main__':
    side_length = 5
    area = square_area(side_length)
    print(area)