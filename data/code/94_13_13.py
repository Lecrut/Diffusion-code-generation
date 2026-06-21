def check_sequence_condition(iterable, condition):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    if not callable(condition):
        raise ValueError("Condition must be callable")
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            return False
        if condition(item):
            return True

if __name__ == '__main__':
    data = [0, 0, 0, 5, 0]
    func = lambda x: x > 0
    output = check_sequence_condition(data, func)
    print(output)