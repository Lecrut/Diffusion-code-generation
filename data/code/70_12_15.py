def extract_boundary_items(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(sequence) == 0:
        raise ValueError("Input sequence cannot be empty")
    
    first_item = sequence[0]
    last_item = sequence[-1]
    return first_item, last_item

if __name__ == '__main__':
    data_values = [42, 17, 8, 99, 3]
    result_first, result_last = extract_boundary_items(data_values)
    print(result_first, result_last)