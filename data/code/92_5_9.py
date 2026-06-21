def _validate_boolean(item):
    if not isinstance(item, bool):
        raise ValueError(f"Expected bool, got {type(item).__name__}")
    return item

def yield_opposite_truths(iterable):
    for item in iterable:
        _validate_boolean(item)
        yield not item

if __name__ == '__main__':
    sample_values = [True, False, True, False, True]
    result = list(yield_opposite_truths(sample_values))
    print(result)