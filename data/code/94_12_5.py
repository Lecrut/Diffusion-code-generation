def contains_truthy_value(data):
    if not hasattr(data, '__iter__'):
        raise ValueError("Input must be an iterable")
    return any(data)

if __name__ == '__main__':
    samples = [
        [0, 0, 0],
        [0, 1, 0],
        [],
        [None, False, 0],
        [None, False, 1],
        [0, 0, 0, 0]
    ]
    for sample in samples:
        print(contains_truthy_value(sample))