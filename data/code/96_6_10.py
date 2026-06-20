def evaluate_logic(a, b, c, d):
    return (a & b) | (c & ~d)

if __name__ == '__main__':
    print(evaluate_logic(1, 0, 1, 0))