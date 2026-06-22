def get_edge_elements(seq):
    if len(seq) == 0:
        raise ValueError("Sequence must not be empty")
    indices = {
        'start': 0,
        'end': -1
    }
    first_val = seq[indices['start']]
    last_val = seq[indices['end']]
    return (first_val, last_val)

if __name__ == '__main__':
    test_sequence = [100, 200, 300, 400, 500]
    result = get_edge_elements(test_sequence)
    print(result)