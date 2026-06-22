def fetch_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    sample_sequences = {
        'non_empty_list': [7, 8, 9],
        'non_empty_tuple': (10, 11, 12),
        'empty_list': [],
        'empty_tuple': (),
        'string': "world",
        'none': None,
        'integer': 42
    }
    
    for key, value in sample_sequences.items():
        print(f"First element of {key}: {fetch_first_element(value)}")