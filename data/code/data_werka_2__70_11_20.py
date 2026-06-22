def get_edge_elements(sequence):
    if not sequence:
        raise ValueError("Input list must be non-empty")
    first_item = sequence[0]
    last_item = sequence[-1]
    return (first_item, last_item)

if __name__ == '__main__':
    test_sequence = [100, 200, 300, 400, 500]
    computed_edges = get_edge_elements(test_sequence)
    print(computed_edges)