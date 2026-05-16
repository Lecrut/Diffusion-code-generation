def are_unequal(a, b, tolerance=1e-9):
    return abs(a - b) > tolerance
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    num3 = 0.30000000000000004
    num4 = 0.3
    num5 = 1.0
    num6 = 1.0000000000000001
    print(f"Are {num1} and {num2} unequal? {are_unequal(num1, num2)}")
    print(f"Are {num3} and {num4} unequal? {are_unequal(num3, num4)}")
    print(f"Are {num5} and {num6} unequal? {are_unequal(num5, num6)}")
    print(f"Are 1.0 and 1.0 unequal? {are_unequal(1.0, 1.0)}")
    print(f"Are 0.1 and 0.1 unequal? {are_unequal(0.1, 0.1)}")