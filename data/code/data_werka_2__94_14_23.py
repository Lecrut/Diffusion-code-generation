def contains_true(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        return False
    iterator = iter(values)
    while True:
        try:
            current = next(iterator)
        except StopIteration:
            return False
        if current is True:
            return True
        if current == True and not isinstance(current, bool):
            continue
        if isinstance(current, bool):
            if current:
                return True
    return False

if __name__ == '__main__':
    sample_input = [False, False, False, True, False]
    result = contains_true(sample_input)
    print(result)