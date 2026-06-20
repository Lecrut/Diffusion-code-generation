def any_truthy(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    return any(iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], {}, (), '']
    print(any_truthy(sample_values))