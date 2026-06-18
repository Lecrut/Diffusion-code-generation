def reverse_sequence(seq):
    if isinstance(seq, (list, tuple)):
        return type(seq)(reverse_sequence(item) for item in reversed(seq))
    elif isinstance(seq, dict):
        new_dict = {}
        for key, value in seq.items():
            new_dict[reversed(key)] = reverse_sequence(value)
        return new_dict
    else:
        raise TypeError("Unsupported sequence type")
if __name__ == '__main__':
    sample_data = [1, 2, 3]