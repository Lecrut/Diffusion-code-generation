def get_last_element(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Expected a list or tuple")
    if len(seq) == 0:
        raise ValueError("Sequence must be non-empty")
    return seq[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_element(sample_list)
    print(result)