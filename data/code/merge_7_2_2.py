def are_equal_xor(x, y):
    return (x ^ y) == 0
if __name__ == '__main__':
    x1 = 10
    y1 = 10
    print(f"x={x1}, y={y1}: {are_equal_xor(x1, y1)}")
    x2 = 5
    y2 = 3
    print(f"x={x2}, y={y2}: {are_equal_xor(x2, y2)}")
    x3 = 1234567890
    y3 = 1234567890
    print(f"x={x3}, y={y3}: {are_equal_xor(x3, y3)}")
    x4 = 99
    y4 = 100
    print(f"x={x4}, y={y4}: {are_equal_xor(x4, y4)}")