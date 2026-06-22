def compute_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

if __name__ == '__main__':
    example_side = 7
    print(compute_area(example_side))