def _validate_non_empty_sequence(seq):
    if not seq:
        raise ValueError("Sequence must not be empty")

def get_boundary_items(collection):
    _validate_non_empty_sequence(collection)
    return collection[0], collection[-1]

if __name__ == '__main__':
    words = ["start", "middle", "end"]
    first_item, last_item = get_boundary_items(words)
    print(first_item)
    print(last_item)