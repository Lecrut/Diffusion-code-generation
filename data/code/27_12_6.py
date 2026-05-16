import math
def are_unequal(a, b, epsilon=1e-9):
    return abs(a - b) > epsilon
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    num3 = 0.30000000000000004
    num4 = 1.0
    num5 = 1.0000000000000002
    print(f"num1: {num1}, num2: {num2}")
    print(f"Are num1 and num2 unequal? {are_unequal(num1, num2)}")
    print("-" * 20)
    print(f"num3: {num3}, num4: {num4}")
    print(f"Are num3 and num4 unequal? {are_unequal(num3, num4)}")
    print("-" * 20)
    print(f"num5: {num5}, num4: {num4}")
    print(f"Are num5 and num4 unequal? {are_unequal(num5, num4)}")