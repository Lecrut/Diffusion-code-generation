def evaluate_inequality(x, y):
    try:
        return x <= y
    except TypeError:
        raise ValueError('Both inputs must be comparable types.')
if __name__ == '__main__':
    print(evaluate_inequality(3, 5))
    print(evaluate_inequality(10, 10))
    print(evaluate_inequality('a', 'b'))
    print(evaluate_inequality([1, 2], [1, 3]))
    try:
        print(evaluate_inequality(3, '5'))
    except ValueError as e:
        print(e)