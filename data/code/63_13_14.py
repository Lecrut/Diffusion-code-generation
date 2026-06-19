def fetch_first_element(sequence):
    return sequence[0] if isinstance(sequence, (list, tuple)) and len(sequence) > 0 else None

if __name__ == '__main__':
    sample_sequences = {
        'non_empty_list': [1, 2, 3],
        'non_empty_tuple': (4, 5, 6),
        'empty_list': [],
        'empty_tuple': (),
        'string': "hello",
        'none': None,
        'number': 123
    }
    
    for key, value in sample_sequences.items():
        print(f"First element of {key}: {fetch_first_element(value)}")