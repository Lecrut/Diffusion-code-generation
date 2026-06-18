def find_max_index(lst):
    """Recursively finds the index of the largest element in a list."""
    if len(lst) == 1:
        return 0
    else:
        max_idx = find_max_index(lst[:-1])
        current_val = lst[max_idx]
        next_val = lst[-1]
        if current_val > next_val:
            return max_idx
        elif current_val < next_val:
            return len(lst) - 1
    # Handle empty list case by returning None, though problem implies valid input

def is_max_larger_than_target(numbers_list, target):
    """Recursively determines if the largest element in numbers_list is larger than target."""
    if not isinstance(numbers_list, list):
        raise TypeError("Input must be a list")
    
    base_case = len(numbers_list) == 0
    
    if base_case:
        return False # No elements cannot satisfy condition

    def recursive_helper(sub_list):
        """Helper to find the index of max in sub_list."""
        n = len(sub_list)
        if n == 1:
            return 0
        
        idx_max_of_rest, val_max_of_rest = recursive_helper(sub_list[:-1])
        
        rest_val = sub_list[idx_max_of_rest]
        last_val = sub_list[-1]

        # Compare max of rest with the current element at end
        if rest_val > last_val:
            index_in_full = idx_max_of_rest
        else:
            index_in_full = n - 1
        
        value_at_index = numbers_list[index_in_full]
        
        return value_at_index

    # Recursively find max of the list by reducing size and comparing with head/tail logic
    def get_recursive_max(lst):
        if not lst:
            raise ValueError("Cannot determine max from empty list")
            
        n = len(lst)
        if n == 1:
            return lst[0]

        # Recursive call on the sublist excluding the last element (or first, doesn't matter for logic depth)
        max_of_rest = get_recursive_max(lst[:-1])
        
        current_elem = lst[-1]

        final_result = max(max_of_rest, current_elem) if n > 0 else None
        
        return final_result
    
    # Since task asks for recursive function specifically to determine condition

if __name__ == '__main__':
    pass
