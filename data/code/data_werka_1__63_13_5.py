def is_non_empty_sequence(sequence):
    return isinstance(sequence, (list, tuple)) and len(sequence) > 0

def get_first_element(sequence):
    if is_non_empty_sequence(sequence):
        return sequence[0]
    return None

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        (4, 5, 6),
        [],
        (),
        "hello",
        None,
        123
    ]
    for value in sample_values:
        print(get_first_element(value))