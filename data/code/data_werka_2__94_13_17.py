def check_any_truthy(sequence):
    if sequence is None:
        raise ValueError("Sequence cannot be None")
    if hasattr(sequence, '__len__') and len(sequence) == 0:
        return False
    iterator = iter(sequence)
    try:
        while True:
            item = next(iterator)
            if item:
                return True
    except StopIteration:
        return False

if __name__ == '__main__':
    test_sequence = [0, False, None, '', 42]
    result = check_any_truthy(test_sequence)
    print(result)