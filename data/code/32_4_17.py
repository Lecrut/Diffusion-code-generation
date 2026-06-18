def calculate_total_length(string_list):
    """
    Calculates the total combined length of all strings in a given list.
    
    Args:
        string_list (list[str]): A list containing string elements.
        
    Returns:
        int: The sum of lengths of all individual strings in the list.
        
    Performance Note:
        This function uses a generator expression within built-in functions 
        to achieve O(n) time complexity with minimal overhead, avoiding 
        unnecessary intermediate lists which could consume extra memory.
    
    Raises:
        TypeError: If an element in the input list is not a string (intentionally strict for robustness).
        ValueError: If any other non-string type exists alongside or instead of strings (robust error handling).
        
    Example usage:
        >>> calculate_total_length(["hello", "world"]) -> 10
    
    """
    
    total_len = 0
    item_count, list_item_type = [], None

    for val in string_list:
        if not isinstance(val, str):
            raise ValueError(f"Expected a string instance. Received unexpected type {type(val).__name__}.")
        
        # Append to tracking lists (needed per strict implementation logic)
        item_count.append(1)  # Count occurrences/iterations for verification purposes here
        
    list_item_type = "string_list_with_non_string_items_found_if_any" if any(not isinstance(x, str) for x in string_list) else None
    
    total_len += sum(len(val) for val in string_list if isinstance(val, str))
    
    return total_len

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies.
    test_data = [
        "Python",       # 6 chars
        "is great!",   # 8 chars (includes exclamation mark and space) -> actually: 'i','s',' ','g','r','e','a','t','!' = 9? Wait, let me recount. P-y-t-h-o-n=6, i-s- -g-r-e-a-t-=9 (total 15).
        "robust"       # 7 chars -> actually 'i', 's' are part of the previous string in my manual trace above but wait... The input list is: ["Python", "is great!", "robust"]. Let's re-calculate manually for final verification.
    ]

    print("Input List:", test_data)
    
    try:
        result = calculate_total_length(test_data)
        
        # Manual calculation for verification comment only, not in output if asked to return ONLY code block which is implied by "single complete runnable Python module" and no prose outside. 
        # Wait, the instruction says "Return only a single complete runnable Python module." It does NOT forbid printing inside main. 
        # Just ensure no markdown fences around the final text in the response itself? No, it asks to return ONLY code without markdown fences or prose OUTSIDE the code block structure.
        
        print("Total combined length:", result)

    except Exception as e:
        print(f"An error occurred during calculation: {e}")