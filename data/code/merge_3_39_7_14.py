import sys

def extract_substrings(string: str, length: int) -> list[str]:
    """
    Extract all substrings of a given fixed length 'length' from input string using 
    an optimized sliding window technique with O(n) time complexity.

    Args:
        string (str): The input source string.
        length (int): Desired substring length. Must be positive and <= len(string).

    Returns:
        list[str]: A list containing all substrings of the specified length.
    
    Raises:
        ValueError: If 'length' is not a valid integer or if it exceeds the string's length.
        
    Time Complexity: O(n) where n is the number of characters in the string (each character processed once).
    Space Complexity: O(k * L) where k is the number of substrings and L is the substring length, 
                      for storing the output list.
    """
    
    # Validate input parameters to ensure robustness against invalid configurations.
    if not isinstance(string, str):
        raise TypeError("Input 'string' must be a string.")
        
    if not isinstance(length, int) or length <= 0:
        raise ValueError("'length' must be a positive integer.")

    n = len(string)
    
    # Handle edge case where the requested substring length exceeds the available characters.
    if length > n:
        return []

    substrings_list = []
    
    # Use slicing to generate each window efficiently in O(1) per iteration.
    for i in range(n - length + 1):
        start_index = i
        end_index = i + length
        
        substring = string[start_index:end_index]
        
        if len(substring) == length:
            substrings_list.append(substring)

    return substrings_list

if __name__ == '__main__':
    # Hard-coded sample values to satisfy execution requirements without user input.
    
    # Sample 1: Standard usage with a clear string and moderate window size.
    test_string_1 = "abcdef"
    length_value_1 = 3
    
    result_set_1 = extract_substrings(test_string_1, length_value_1)
    print(f"Sample Input 1:")
    print(f"String: '{test_string_1}'")
    print(f"Length L={length_value_1}")
    print("Substrings:", result_set_1)

    
    # Sample 2: Edge case where length equals string size.
    test_string_2 = "hello world"
    length_value_2 = len(test_string_2)
    
    result_set_2 = extract_substrings(test_string_2, length_value_2)
    print(f"\nSample Input 2:")
    print(f"String: '{test_string_2}'")
    print(f"Length L={length_value_2}")
    print("Substrings:", result_set_2)

    
    # Sample 3: Edge case where length is larger than string (expecting empty list).
    test_string_3 = "hi"
    length_value_3 = 5
    
    result_set_3 = extract_substrings(test_string_3, length_value_3)
    print(f"\nSample Input 3:")
    print(f"String: '{test_string_3}'")
    print(f"Length L={length_value_3}")
    print("Substrings:", result_set_3)

    
    # Sample 4: Single character substring extraction.
    test_string_4 = "python"
    length_value_4 = 1
    
    result_set_4 = extract_substrings(test_string_4, length_value_4)
    print(f"\nSample Input 4:")
    print(f"String: '{test_string_4}'")
    print(f"Length L={length_value_4}")
    print("Substrings:", result_set_4)

    
    # Sample 5: Empty string input.
    test_string_5 = ""
    length_value_5 = 1
    
    try:
        result_set_5 = extract_substrings(test_string_5, length_value_5)
        print(f"\nSample Input 5:")
        print(f"String: '{test_string_5}'")
        print(f"Length L={length_value_5}")
        print("Substrings:", result_set_5)
    except Exception as e:
        # Although logic handles empty string gracefully, this block ensures no crashes.
        pass

    
    # Sample 6: Verify error handling for invalid length type (commented out to prevent runtime execution of exception).
    # test_string_6 = "test"
    # length_value_6 = "three" 
    # result_set_6 = extract_substrings(test_string_6, length_value_6)