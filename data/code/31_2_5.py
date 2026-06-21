def area_of_square(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    if side == int(side):
        side = int(side)
        return side * side
    return side ** 2

if __name__ == '__main__':
    print(area_of_square(5))
    print(area_of_square(3.5))