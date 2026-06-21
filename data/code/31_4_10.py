def compute_square_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    if side == 0:
        return 0
    return side * side

if __name__ == '__main__':
    print(compute_square_area(7))
    print(compute_square_area(0))
    print(compute_square_area(3))