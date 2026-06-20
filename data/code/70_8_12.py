def is_valid_sequence(seq):
    return isinstance(seq, (list, tuple))

def check_sequence(seq):
    if not is_valid_sequence(seq):
        raise ValueError("Input must be a list or tuple.")
    if not seq:
        return (None, None)
    return (seq[0], seq[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    print(check_sequence(sample_list))
    print(check_sequence(sample_tuple))
    print(check_sequence(empty_list))
    print(check_sequence(empty_tuple))