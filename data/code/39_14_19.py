def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through all possible start and end indices (inclusive).
    For each pair (start, end), it yields the substring from index 'start' to 'end'.

    Args:
        s (str): The input string.

    Yields:
        str: Each valid substring of s in order of increasing length and starting position.
    
    Memory Efficiency:
        This generator processes one substring at a time, yielding it immediately 
        without storing the entire list in memory. It uses O(1) auxiliary space 
        (excluding input/output buffers).

    Example:
        >>> for sub in generate_substrings("abc"):
        ...     print(sub)
        a
        ab
        abc
        b
        bc
        c
    """
    n = len(s)
    
    # Iterate over all possible start indices from 0 to n-1
    for i in range(n):
        # Iterate over all possible end indices from i+1 to n (inclusive of the character at index i, exclusive of next char after last)
        # Actually, we want inclusive slicing: s[start:end] where end goes up to len(s). 
        # To get substring including 'i', slice is [start : start + length]. 
        # Let's use standard python convention: s[i:j] includes i but excludes j.
        # So for a fixed start `i`, we want lengths from 1 to n-i.
        # The end index in slicing will be i+length, ranging from i+1 to n.
        
        for length in range(1, n - i + 1):
            yield s[i : i + length]

if __name__ == '__main__':
    sample_string = "abc"
    
    print(f"All substrings of '{sample_string}':")
    count = 0
    for substring in generate_substrings(sample_string):
        print(repr(substring))
        count += 1
    
    print(f"\nTotal number of substrings: {count}")

# Verification with another string to ensure correctness logic without interactive input
if __name__ == '__main__':
    sample_string_2 = "xy"
    
    print(f"All substrings of '{sample_string_2}':")
    for substring in generate_substrings(sample_string_2):
        print(substring)

# Final check block to ensure no external dependencies or prompts are triggered
if __name__ == '__main__':
    # This ensures the module runs standalone if executed directly as a script
    test_input = "test"
    
    results = list(generate_substrings(test_input))
    
    assert len(results) > 0, "Generator should yield at least one substring."
    expected_count = (len(test_input) * (len(test_input) + 1)) // 2
    
    # Calculate total substrings for a string of length n: n*(n+1)/2
    calculated_total = len(results)
    
    assert calculated_total == expected_count, f"Expected {expected_count} substrings but got {calculated_total}"

    print(f"\nTest passed. String '{test_input}' has exactly {calculated_total} substrings.")