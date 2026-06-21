def _validate_sequence(item):
    try:
        length = len(item)
    except TypeError:
        raise ValueError("Input must support len()")
    try:
        item[0]
        item[-1]
    except (TypeError, IndexError):
        if length == 0:
            return False
        raise ValueError("Input must support indexing")
    return True

def get_sequence_boundaries(sequence):
    if not _validate_sequence(sequence):
        raise ValueError("Input must be a non-empty sequence")
    return (sequence[0], sequence[-1])

if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    data_tuple = (10, 20, 30)
    data_str = "python"
    data_set = {99}
    print(get_sequence_boundaries(data_list))
    print(get_sequence_boundaries(data_tuple))
    print(get_sequence_boundaries(data_str))
    print(get_sequence_boundaries(data_set))