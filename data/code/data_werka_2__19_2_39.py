def evaluate_inequality(x, y):
    try:
        return x <= y
    except TypeError:
        raise ValueError('Both x and y must be comparable types.')
if __name__ == '__main__':
    print(evaluate_inequality(3, 5))
    print(evaluate_inequality(10, 10))
    print(evaluate_inequality(7, 2))
    print(evaluate_inequality('a', 'b'))
    print(evaluate_inequality('c', 'a'))