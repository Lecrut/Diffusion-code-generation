def find_middle_index(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 0:
        middle_idx = (length // 2) - 1
        left_val, right_val = sequence[middle_idx], sequence[middle_idx + 1]
        if left_val < right_val:
            final_idx = middle_idx
        else:
            final_idx = middle_idx + 1
    else:
        middle_idx = length // 2
    return {
        'index': middle_idx, 
        'value_at_index': sequence[middle_idx],
        'is_even_length': (length % 2 == 0),
        'left_neighbor': None if is_even_length and left_val < right_val else (sequence[middle_idx] if not is_even_length else None)                                                     
    }
def get_middle_index(sequence):
    n = len(sequence)
    if n == 0:
        return {"index": -1, "value": None}
    if n % 2 == 0:
        idx = n // 2
    else:
        idx = n // 2
    return {"index": idx, "value": sequence[idx]}
if __name__ == '__main__':
    test_cases = [
        [], 
        [1], 
        [1, 2], 
        [1, 2, 3], 
        [10, 20, 30, 40]
    ]
    for seq in test_cases:
        result = get_middle_index(seq)
        print(f"Input: {seq} -> Index: {result['index']}, Value: {result['value']}")