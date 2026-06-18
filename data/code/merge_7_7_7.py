def are_close(a, b, epsilon=1e-9):
    return abs(a - b) <= epsilon
if __name__ == '__main__':
    a1 = 0.1 + 0.2
    b1 = 0.3
    epsilon = 1e-9
    print(f"a1: {a1}, b1: {b1}")
    print(f"Are a1 and b1 close? {are_close(a1, b1, epsilon)}")
    a2 = 1.0 / 3.0
    b2 = 0.3333333333333333
    print(f"a2: {a2}, b2: {b2}")
    print(f"Are a2 and b2 close? {are_close(a2, b2, epsilon)}")
    a3 = 1.0
    b3 = 1.0000000000000001
    print(f"a3: {a3}, b3: {b3}")
    print(f"Are a3 and b3 close? {are_close(a3, b3, epsilon)}")
    a4 = 1.0
    b4 = 1.0 + 1e-8
    print(f"a4: {a4}, b4: {b4}")
    print(f"Are a4 and b4 close? {are_close(a4, b4, epsilon)}")
    a5 = 1.0
    b5 = 1.0 + 1e-7
    print(f"a5: {a5}, b5: {b5}")
    print(f"Are a5 and b5 close? {are_close(a5, b5, epsilon)}")