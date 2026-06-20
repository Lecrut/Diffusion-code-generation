def any_truthy(iterable):
    if not isinstance(iterable, (list, tuple, dict, set)):
        raise ValueError("Input must be an iterable")
    return any(bool(item) for item in iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], {}, (), '']
    try:
        print(any_truthy(sample_values))
    except ValueError as e:
        print(e)