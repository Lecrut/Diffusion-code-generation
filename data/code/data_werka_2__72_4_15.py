def extract_pair_at_index(primary_sequence, secondary_sequence, position):
    minimum_valid_index = 0
    primary_limit = len(primary_sequence)
    secondary_limit = len(secondary_sequence)

    if position < minimum_valid_index:
        raise ValueError("Negative index is not supported")
    
    if position >= primary_limit:
        raise ValueError("Index exceeds bounds of first sequence")
    
    if position >= secondary_limit:
        raise ValueError("Index exceeds bounds of second sequence")

    value_from_first = primary_sequence[position]
    value_from_second = secondary_sequence[position]
    
    return [(value_from_first, value_from_second)]

if __name__ == '__main__':
    data_a = [100, 200, 300]
    data_b = [1.1, 2.2, 3.3]
    target_pos = 2
    fetched = extract_pair_at_index(data_a, data_b, target_pos)
    print(fetched)