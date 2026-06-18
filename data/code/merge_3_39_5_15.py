import sys

def substring_generator(s):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Memory-efficient approach: Yields substrings one by one instead of storing 
    them in memory, suitable for very long strings where the total number 
    of substrings (n*(n+1)/2) would be too large to materialize at once.

    Args:
        s (str): The input string whose substrings are to be generated.

    Yields:
        str: Each substring starting from index i and ending before j, where 
             0 <= i < j <= len(s).
    """
    n = len(s)
    
    # Iterate over all possible start indices
    for i in range(n):
        # For each start index, iterate over end indices to form substrings
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    
    # Test with a small string first
    test_string = "ABC"
    
    print(f"Generating substrings for: '{test_string}'")
    count = 0
    result_list = []
    
    for substring in substring_generator(test_string):
        result_list.append(substring)
        count += 1
    
    # Since the generator is memory efficient, we can also iterate directly 
    # without storing all if needed. Here we store to verify completeness for small input.
    print(f"Total substrings generated: {count}")
    
    sorted_substrings = sorted(result_list)
    expected_count = len(test_string) * (len(test_string) + 1) // 2
    
    assert count == expected_count, "Mismatch in substring count!"
    
    # Print some examples for verification
    print("Sample substrings:")
    for sub in result_list[:5]:
        print(f"  '{sub}'")
    
    # Demonstrate direct iteration (memory efficient mode) without storing all
    sample_long = "A" * 10 + "B"
    long_count = sum(1 for _ in substring_generator(sample_long))
    assert long_count == len(sample_long) * (len(sample_long) + 1) // 2
    
    print(f"\nTest with longer string ('{sample_long}'): Total substrings: {long_count}")