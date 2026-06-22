def check_any_match(iterable, predicate):
    if not callable(predicate):
        raise ValueError("predicate must be a callable")
    iterator = iter(iterable)
    try:
        while True:
            value = next(iterator)
            if predicate(value):
                return True
    except StopIteration:
        return False

if __name__ == '__main__':
    data = [False, 0, None, [], 42, 'non-empty']
    test_predicate = lambda x: bool(x)
    outcome = check_any_match(data, test_predicate)
    print(outcome)