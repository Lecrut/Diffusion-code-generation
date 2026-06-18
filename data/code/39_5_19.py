def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    This implementation is memory-efficient as it does not construct or store 
    the list of all substrings in memory before yielding them. Instead, it uses
    nested loops to calculate start and end indices on-the-fly for each substring.

    Args:
        s (str): The input string from which substrings are generated.

    Yields:
        str: Substrings starting at index i with length j (where 0 <= i < len(s) 
             and 1 <= j such that start + j - 1 < len(s)).
    
    Example usage:
        >>> list(generate_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c'] (order depends on implementation logic, typically length-first or index-first)
        
        Note: The order of yielding is determined by iterating start from 0 to len(s)-1 
        and end from start+1 to len(s), which produces substrings in increasing order 
        of starting position, then increasing order of ending position.
    """
    length = len(s)
    
    # Iterate over all possible starting positions
    for i in range(length):
        # Iterate over all possible lengths or equivalently ending positions
        # We iterate j from 1 to (length - i) inclusive, representing the number of characters included.
        # Alternatively using end_index: start at i+1 up to length.
        for j in range(i + 1, length + 1):
            yield s[i:j]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    
    # Sample string: "ABC" - expected substrings based on logic above
    test_string = "ABC"
    
    print(f"Generating all substrings for the string '{test_string}':")
    count = 0
    result_list = []
    
    # Collect results in a list here just to demonstrate output, 
    # though the generator itself is memory efficient during iteration.
    for substring in generate_substrings(test_string):
        print(f"Substring: {substring}")
        result_list.append(substring)
        count += 1
    
    print(f"\nTotal substrings generated: {count}")
    
    # Additional verification with a longer string to ensure logic holds without memory explosion during generation
    long_test = "abcdefghij"
    print(f"\nGenerating substrings for '{long_test}' (length={len(long_test)}):")
    count_long = 0
    
    for sub in generate_substrings(long_test):
        count_long += 1
        
        # Optional: limit printing to avoid overwhelming console output while testing logic
        if count_long <= 5 or count_long >= len(generate_substrings(long_test)) - 2:
            print(f"Length {len(sub)} | Substring: '{sub}'")
    
    expected_total = (10 * 11) // 2 # n*(n+1)/2 for substrings of length n string? 
                                     # Actually sum(n-i+1 for i in range(n)) = n + (n-1) + ... + 1 = n(n+1)/2
    print(f"\nTotal expected substrings check: {count_long} == {(len(long_test)*(len(long_test)+1))//2}")