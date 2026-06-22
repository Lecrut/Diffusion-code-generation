def get_edge_elements(seq):
    if not hasattr(seq, '__len__') or len(seq) == 0:
        raise ValueError("Input must be a non-empty sequence")
    start_index = 0
    end_index = -1
    first_value = seq[start_index]
    last_value = seq[end_index]
    return (first_value, last_value)

if __name__ == '__main__':
    test_collection = [9, 18, 27, 36, 45]
    edge_pair = get_edge_elements(test_collection)
    print(edge_pair)