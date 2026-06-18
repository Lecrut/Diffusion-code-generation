def float_equality(a, b, epsilon=1e-9):
    return abs(a - b) < epsilon
if __name__ == '__main__':
    a1 = 0.1 + 0.2
    b1 = 0.3
    a2 = 1.0 / 3.0
    b2 = 0.3333333333333333
    a3 = 1.0
    b3 = 1.0000000000000001
    print(f"Checking {a1} and {b1}: {float_equality(a1, b1)}")
    print(f"Checking {a2} and {b2}: {float_equality(a2, b2)}")
    print(f"Checking {a3} and {b3}: {float_equality(a3, b3)}")