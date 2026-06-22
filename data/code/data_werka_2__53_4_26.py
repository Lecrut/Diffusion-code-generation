def compute_square_area(side):
    if side <= 0:
        raise ValueError('Side length must be positive')
    return side * side
if __name__ == '__main__':
    try:
        print(compute_square_area(5))
        print(compute_square_area(-3))
    except ValueError as e:
        print(e)