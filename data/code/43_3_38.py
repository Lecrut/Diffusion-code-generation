def compute_square_area(side):
    return side * side if side >= 0 else None

if __name__ == '__main__':
    test_sides = [2, 4, 6]
    for side in test_sides:
        print(f"Area of square with side {side}: {compute_square_area(side)}")