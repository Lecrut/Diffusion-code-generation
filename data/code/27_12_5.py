import math
def are_unequal(a: float, b: float, epsilon: float = 1e-9) -> bool:
    return abs(a - b) > epsilon
if __name__ == '__main__':
    a1 = 0.1 + 0.2
    b1 = 0.3
    a2 = 1.0
    b2 = 1.0000000000000001
    a3 = 5.0
    b3 = 5.0
    a4 = -0.0
    b4 = 0.0
    print(f"a1: {a1}, b1: {b1}, Unequal: {are_unequal(a1, b1)}")
    print(f"a2: {a2}, b2: {b2}, Unequal: {are_unequal(a2, b2)}")
    print(f"a3: {a3}, b3: {b3}, Unequal: {are_unequal(a3, b3)}")
    print(f"a4: {a4}, b4: {b4}, Unequal: {are_unequal(a4, b4)}")