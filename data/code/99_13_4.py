def evaluate_flags(a, b, c):
    return a or (b and c)

if __name__ == '__main__':
    print(evaluate_flags(True, False, True))
    print(evaluate_flags(False, True, False))
    print(evaluate_flags(False, False, True))
    print(evaluate_flags(False, False, False))