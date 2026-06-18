import sys

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Memory efficiency is achieved by yielding items one at a time rather than 
    storing them in a list, allowing the generator to handle very long strings
    without loading all substrings into memory simultaneously.
    
    Args:
        s (str): The input string for which substrings are generated.
        
    Yields:
        str: Substrings of length 1 up to len(s). Within each length, 
             substrings start from the leftmost character and move rightward.
             
    Example:
        >>> list(generate_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    n = len(s)
    
    # Iterate through all possible lengths of substrings, from 1 to the length of s.
    for i in range(1, n + 1):
        start_index = -1
        
        while True:
            if not (0 <= start_index < n and (start_index + i) >= len(s)):
                break
                
            substring = s[start_index:start_index+i]
            
            # Yield the current substring immediately. 
            # This allows processing to happen as soon as a substring is found,
            # rather than buffering it or storing all substrings in memory.
            yield substring
            
            start_index += 1

if __name__ == '__main__':
    # Hard-coded sample values for testing the generator without user input.
    sample_string = "abcdef"
    
    print(f"Generating substrings from: {sample_string}")
    
    count = 0
    
    # Collect and verify all generated substrings (note: in a real-world scenario with very long strings, 
    # this list collection step would be avoided or replaced by streaming processing logic).
    for substring in generate_substrings(sample_string):
        print(f"Substring [{count}]: {substring}")
        count += 1
        
    total_count = sum(1 for _ in generate_substrings("xyz"))
    
    # Verify the generator works correctly on a smaller string by counting expected results.
    expected_total = (len("xyz") * (len("xyz") + 1)) // 2
    
    print(f"\nVerification:")
    print(f"Total substrings generated for 'xyz': {total_count}")
    print(f"Expected total: {expected_total}")
    
    if total_count == expected_total:
        print("Test passed!")
    else:
        print("Test failed! There is an issue with the generator.")