def fetch_pair_from_index(source_a, source_b, target_index):
    if not isinstance(source_a, (list, tuple)):
        raise TypeError("First argument must be a sequence")
    if not isinstance(source_b, (list, tuple)):
        raise TypeError("Second argument must be a sequence")
    if not isinstance(target_index, int):
        raise TypeError("Index must be an integer")
    
    limit_a = len(source_a)
    limit_b = len(source_b)
    
    if target_index < 0:
        raise ValueError("Index cannot be negative")
    if target_index >= limit_a:
        raise ValueError(f"Index {target_index} is out of range for first list (size {limit_a})")
    if target_index >= limit_b:
        raise ValueError(f"Index {target_index} is out of range for second list (size {limit_b})")
    
    val_a = source_a[target_index]
    val_b = source_b[target_index]
    
    return [(val_a, val_b)]

if __name__ == '__main__':
    data_first = [100, 200, 300, 400]
    data_second = ['x', 'y', 'z', 'w']
    idx_target = 2
    
    computed_result = fetch_pair_from_index(data_first, data_second, idx_target)
    print(computed_result)