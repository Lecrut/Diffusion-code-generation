def _validate_non_empty_sequence(seq):
    if not seq:
        raise ValueError("Sequence must contain at least one element")

def _get_boundary_items(seq):
    _validate_non_empty_sequence(seq)
    return seq[0], seq[-1]

def print_first_and_last(strings):
    first, last = _get_boundary_items(strings)
    print(first)
    print(last)

if __name__ == '__main__':
    sample_data = ["first_item", "middle_item_1", "middle_item_2", "last_item"]
    print_first_and_last(sample_data)