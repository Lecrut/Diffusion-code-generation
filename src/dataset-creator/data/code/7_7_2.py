import math
def float_equality(a, b, epsilon=1e-9):
    return abs(a - b) < epsilon
if __name__ == '__main__':
    a1 = 1.0
    b1 = 1.0000000000000002
    a2 = 0.1 + 0.2
    b2 = 0.3
    a3 = 1.0 / 3.0
    b3 = 0.3333333333333333
    print(f"Checking {a1} and {b1}: {float_equality(a1, b1)}")
    print(f"Checking {a2} and {b2}: {float_equality(a2, b2)}")
    print(f"Checking {a3} and {b3}: {float_equality(a3, b3)}")
    a4 = 1.0
    b4 = 1.0 + 1e-8
    print(f"Checking {a4} and {b4}: {float_equality(a4, b4)}")