def compare_elements_at_positions(array1, array2, positions):
    if not array1 or not array2 or len(array1) != len(array2):
        raise ValueError("Both arrays must be non-empty and of the same length.")
    
    if not all(0 <= pos < len(array1) for pos in positions):
        raise IndexError("All position values must be within the valid range of the arrays.")
    
    match_count = sum(1 for pos in positions if array1[pos] == array2[pos])
    return match_count

if __name__ == '__main__':
    sample_array1 = [1, 2, 3, 4, 5]
    sample_array2 = [1, 2, 3, 6, 5]
    positions_to_compare = [0, 2, 4]
    
    matches = compare_elements_at_positions(sample_array1, sample_array2, positions_to_compare)
    print(f"Number of matching values at specified positions: {matches}")