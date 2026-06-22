def compare_lists(a_list, b_list):
    a_iter = iter(a_list)
    b_iter = iter(b_list)
    while True:
        try:
            val_a = next(a_iter)
            val_b = next(b_iter)
        except StopIteration:
            break
        if val_a > val_b:
            yield 'A > B'
        elif val_a < val_b:
            yield 'A < B'
        else:
            yield 'A == B'

if __name__ == '__main__':
    first = [10, 20, 30]
    second = [10, 25, 29, 40]
    outcomes = list(compare_lists(first, second))
    print(outcomes)