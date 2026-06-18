if __name__ == '__main__':
    test_cases = [((3, 3), True), ((3.0, 2.5), False), ((3, "3"), False)]
    for vals in test_cases:
        x, y = vals[0] if isinstance(vals[0], list) else (vals[1][0], vals[1][1])
        print(x, "=", y and equal(x, y))