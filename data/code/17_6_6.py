def _validate_sequence(seq):
    if not isinstance(seq, list):
        raise TypeError("Input must be a list")
    if len(seq) == 0:
        raise ValueError("Cannot retrieve last element from an empty list")

def retrieve_tail(sequence):
    _validate_sequence(sequence)
    return sequence[-1]

if __name__ == '__main__':
    test_data = ["apple", "banana", "cherry", "date"]
    tail_value = retrieve_tail(test_data)
    print(tail_value)