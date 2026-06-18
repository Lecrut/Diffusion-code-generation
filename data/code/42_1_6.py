def build_string_from_parts(parts):
    """
    Joins a list of string parts into a single string with spaces as separators.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The joined string separated by spaces.
        
    Time Complexity: O(n), where n is the total number of characters in all strings.
    Space Complexity: O(1) excluding the space required for the output string.
    
    Note: This implementation uses Python's native join method which 
    internally utilizes an optimized C-level algorithm achieving linear time complexity.
    """
    return " ".join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_parts = ["Hello", "World", "This", "Is", "An", "Optimized", "Function"]
    
    result = build_string_from_parts(sample_parts)
    print(result)

# Additional test cases for verification without interactive prompts
test_cases = [
    (["A"], "A"),
    ([], ""),
    (["Single"], "Single"),
    (["One", "Two", "Three"], "One Two Three")
]

for input_list, expected in test_cases:
    output = build_string_from_parts(input_list)
    assert output == expected, f"Failed for {input_list}: got '{output}', expected '{expected}'"
    
print("All tests passed.")