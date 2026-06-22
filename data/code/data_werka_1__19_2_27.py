def evaluate_inequality(x, y):
    try:
        return x <= y
    except TypeError:
        return False
if __name__ == '__main__':
    print(evaluate_inequality(3, 5))
    print(evaluate_inequality('a', 'b'))
    print(evaluate_inequality([1], [2]))
    print(evaluate_inequality(3, '5'))
    print(evaluate_inequality('abc', 10))