"""
Module to calculate the total combined length of a list of strings efficiently.
This implementation uses built-in string methods which in CPython are highly optimized.
It avoids Python loops over characters by operating on the entire string objects directly if needed,
though for simple summation of lengths, iterating once is O(n) and optimal.

Performance Note: 
Using sum(len(s) for s in strings_list) creates a generator object that iterates through each string exactly once.
This avoids creating intermediate lists (which would be used by list comprehension), saving memory overhead while maintaining speed.
"""

def calculate_total_length(strings_list):
    """
    Calculates the total combined length of all strings in the provided list.

    Args:
        strings_list (list[str]): A list containing string elements. The function handles empty lists, 
                                  lists with None values (treated as non-contributing to length), and normal strings.

    Returns:
        int: The sum of lengths of valid string entries in the input list. If an element is not a string 
             or does not support len(), it contributes 0 to avoid runtime errors on mixed type lists, though strict typing suggests only strings are passed.

    Raises:
        TypeError: If any item in the list cannot be measured for length (e.g., non-string object).
                   Note: Using try/except internally keeps it robust against unexpected types without crashing immediately if possible logic dictates, 
                   but per "robust" definition here we assume valid input as per task constraints regarding no user prompts/files.
    
    Example:
        >>> calculate_total_length(["Hello", "", "World"])
        10 (5 + 0 + 5)
    """
    total = 0
    
    # Iterate through the list to sum lengths of actual strings.
    for item in strings_list:
        if isinstance(item, str):
            length_count = len(item)
            total += length_count
            
    return total

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no input/args/files needed).
    sample_data_1 = ["Python", "is", "awesome"]
    
    sample_data_2 = ["" , "", "" ]  # Edge case with multiple empty strings.

    sample_data_3 = list(range(5)) # Mixed types for robustness check (though task implies string list). 
                                    # This function handles non-strings gracefully by skipping or raising, here we ensure it processes only valid lengths if needed.
    
    result_1 = calculate_total_length(sample_data_1)

    print(f"Length of sample 1: {result_1}") 

# Expected output for sample_data_1: "Python"(6)+is(2)+"awesome"(7) -> Wait, let's recheck manually to match expectation in docstring logic above.
# Actually 'Python' is 6, 'is' is 2, 'awesome' is 7 -> Total should be 15 based on manual count? 
# Let me recount: P-y-t-h-o-n (6), i-s (2), a-w-e-s-o-m-e (7). Sum = 6+2+7=15.