"""
Script demonstrating list comprehension vs str.join() optimization.

This script shows two ways to construct a final string from a list of parts:
1. Using list comprehension followed by joining (less efficient).
2. Directly using the join method on an iterable (more efficient as it avoids creating an intermediate list).

Both methods produce identical results, but str.join() is generally preferred for performance 
in Python because it processes strings in C rather than building a temporary list of string objects first."""

def build_string_list_comprehension(parts):
    """
    Constructs a single string from a list using list comprehension.
    
    This method creates an intermediate list by joining parts with newlines, then joins again to combine into one line.
    It is less efficient than direct join() but demonstrates the concept of building lists before processing strings.
    
    Args:
        parts (list): A list of string fragments.
        
    Returns:
        str: The final combined string.
    """
    # Create a temporary list using comprehension to simulate an optimization scenario 
    # where we might want to filter or transform items first, then join.
    filtered_parts = [part for part in parts if len(part) > 0]
    
    # Join the intermediate list with newlines and wrap it again (inefficient step shown here).
    combined_list = ", ".join(filtered_parts.split(", ")) 
    final_result = "\n".join(combined_list) + " [via comprehension approach]"
    return final_result

def build_string_direct_join(parts):
    """
    Constructs a single string from a list using str.join() directly.
    
    This is the optimized approach where we pass the iterable of strings 
    directly to join(), avoiding any intermediate list creation for simple concatenation logic.
    
    Args:
        parts (list): A list of string fragments.
        
    Returns:
        str: The final combined string using direct joining with a delimiter.
    """
    # Directly use the iterable passed in without creating an extra list first.
    # This is the standard optimization for constructing large strings from lists.
    return ", ".join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "Python"]

    result_comprehension = build_string_list_comprehension(sample_parts)
    result_join = build_string_direct_join(sample_parts)

    print("Result via comprehension approach:", repr(result_comprehension))
    print("Result via direct join():", repr(result_join))
    
    # Both results should essentially represent the same logical string content 
    # (ignoring the specific wrapper text added in the example for demonstration).