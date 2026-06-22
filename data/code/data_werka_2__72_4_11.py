def extract_pair_from_lists(primary_sequence, secondary_sequence, position):
    index_map = {"start": 0, "end": -1}
    valid_position = index_map["start"] if position == "start" else (len(primary_sequence) + index_map["end"]) if position == "end" else position
    
    if not isinstance(valid_position, int):
        raise ValueError("Position must be an integer or a valid key")
        
    if valid_position < 0:
        adjusted_position = len(primary_sequence) + valid_position
    else:
        adjusted_position = valid_position

    if adjusted_position < 0 or adjusted_position >= len(primary_sequence):
        raise ValueError("Index out of range for primary sequence")
        
    if adjusted_position < 0 or adjusted_position >= len(secondary_sequence):
        raise ValueError("Index out of range for secondary sequence")

    first_item = primary_sequence[adjusted_position]
    second_item = secondary_sequence[adjusted_position]
    
    return [(first_item, second_item)]

if __name__ == '__main__':
    data_a = [100, 200, 300, 400]
    data_b = ["alpha", "beta", "gamma", "delta"]
    target_pos = 2
    
    extracted_result = extract_pair_from_lists(data_a, data_b, target_pos)
    print(extracted_result)