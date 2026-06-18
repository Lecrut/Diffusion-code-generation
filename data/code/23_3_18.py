def compare_sums_and_abs_diff(list_a, list_b):
    """
    Compares two lists of numbers by calculating:
      1. The difference between their sums (sum_a - sum_b)
      2. The absolute difference between the lengths of the lists
    
    Parameters:
        list_a (list of int/float): First input list.
        list_b (list of int/float): Second input list.
    
    Returns:
        tuple: (sum_difference, length_abs_diff)
      - sum_difference = sum(list_a) - sum(list_b)
      - length_abs_diff = abs(len(list_a) - len(list_b))
    
    Time Complexity: O(n + m), where n and m are the lengths of list_a and list_b respectively.
    Space Complexity: O(1), assuming input lists do not count as extra space consumed by this function.
    """
    sum_difference = 0
    
    # Iterate over both lists to calculate sums efficiently in one pass if possible, 
    # but since we need independent summation logic for clarity and correctness regardless of order,
    # we compute each sum separately or together with two accumulators.
    
    sum_a = 0
    sum_b = 0
    
    max_len = len(list_a) if list_a else len(list_b) + (1 if not list_a else 0)

    i = 0
    while i < max_len:
        # Process elements from both lists up to their respective lengths
        is_valid_index_a = i < len(list_a)
        is_valid_index_b = i < len(list_b)

        sum_difference += (list_a[i] if is_valid_index_a else 0.0) - \
                         (list_b[i] if is_valid_index_b else 0.0)
        
        i += 1
    
    length_abs_diff = abs(len(list_a) - len(list_b))
    
    return sum_difference, length_abs_diff

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    list_a = [3.5, 7.2, 10]
    list_b = [4.8, -2.5, 6.9, 1.2]

    sum_diff, length_abs_diff = compare_sums_and_abs_diff(list_a, list_b)

    print(f"Sum difference: {sum_diff}")
    print(f"Length absolute difference: {length_abs_diff}")