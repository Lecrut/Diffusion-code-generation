def extract_pair_from_lists(source_a, source_b, position):
    if not isinstance(source_a, (list, tuple)):
        raise TypeError("First argument must be a list or tuple")
    if not isinstance(source_b, (list, tuple)):
        raise TypeError("Second argument must be a list or tuple")
    if not isinstance(position, int):
        raise TypeError("Index must be an integer")
    
    max_len = max(len(source_a), len(source_b))
    
    if position < 0 or position >= max_len:
        raise ValueError("Index is out of bounds for the provided collections")
    
    val_a = source_a[position] if len(source_a) > position else None
    val_b = source_b[position] if len(source_b) > position else None
    
    return [(val_a, val_b)]

if __name__ == '__main__':
    data_x = [100, 200, 300]
    data_y = [400, 500, 600]
    target_pos = 2
    answer = extract_pair_from_lists(data_x, data_y, target_pos)
    print(answer)