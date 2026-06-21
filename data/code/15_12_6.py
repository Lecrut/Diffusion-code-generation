def _validate_sequence(seq):
    if not isinstance(seq, list):
        raise TypeError("Input must be a list")
    if len(seq) < 2:
        raise ValueError("List must contain at least two elements")

def get_penultimate_item(seq):
    _validate_sequence(seq)
    return seq[-2]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    print(get_penultimate_item(test_data))