def calculate_square(side):
    if not isinstance(side, int):
        raise TypeError("side must be an integer")
    if side < 0:
        raise ValueError("side must be non-negative")
    return side * side

if __name__ == '__main__':
    test_side = 7
    computed_result = calculate_square(test_side)
    print(computed_result)