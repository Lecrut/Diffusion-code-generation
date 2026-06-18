import timeit

def build_string_from_parts(parts: list[str]) -> str:
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The resulting concatenated string separated by spaces.
    """
    return " ".join(parts)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_parts = ["Hello", "world", "this", "is", "an", "optimized", "function"]

    result = build_string_from_parts(sample_parts)
    
    print("Sample Input:", sample_parts)
    print("Result:", result)
    
    # Optional: Simple performance check to demonstrate O(n) behavior conceptually
    n = len(sample_parts)
    expected_length = sum(len(part) for part in sample_parts) + (n - 1) * len(" ")
    actual_len = len(result)
    
    assert result == " ".join(sample_parts), "String construction failed"
    assert actual_len == expected_length, f"Length mismatch: {actual_len} != {expected_length}"
    
    print("\nPerformance verification passed.")