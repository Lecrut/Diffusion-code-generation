def _validate_sequence(data):
    if not hasattr(data, '__getitem__'):
        raise TypeError("Input must support indexing")
    if not hasattr(data, '__len__'):
        raise TypeError("Input must have a length")
    if len(data) == 0:
        raise ValueError("Sequence cannot be empty")
    return True

def check_first_and_last(seq):
    _validate_sequence(seq)
    return (seq[0], seq[-1])

if __name__ == '__main__':
    sample_sequence = (100, 200, 300, 400, 500)
    result = check_first_and_last(sample_sequence)
    print(result)