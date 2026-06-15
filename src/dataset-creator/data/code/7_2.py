def are_equal_xor(x, y):
    return (x ^ y) == 0
if __name__ == '__main__':
    x1 = 10
    y1 = 10
    print(f"x={x1}, y={y1}, are equal: {are_equal_xor(x1, y1)}")
    x2 = 5
    y2 = 3
    print(f"x={x2}, y={y2}, are equal: {are_equal_xor(x2, y2)}")
    x3 = 7
    y3 = 7
    print(f"x={x3}, y={y3}, are equal: {are_equal_xor(x3, y3)}")
    x4 = 12
    y4 = 15
    print(f"x={x4}, y={y4}, are equal: {are_equal_xor(x4, y4)}")