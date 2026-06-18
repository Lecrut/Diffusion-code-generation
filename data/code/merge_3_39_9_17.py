"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
A substring is considered "nested" if it appears at least twice in the input string (possibly overlapping).
The function returns these unique substrings sorted by length (ascending) and then alphabetically.
"""

def find_nested_substrings(phrase: str):
    """
    Finds all nested substrings within a phrase where a substring occurs more than once.
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique nested substrings found in the phrase.
                   Sorted by length ascending, then alphabetically for ties.
    """
    if not phrase or len(phrase) < 2:
        return []

    # Dictionary to store occurrences (start index -> count is sufficient logic here via set membership check later)
    # We need substrings that appear at least twice.
    
    seen_substrings = set()
    result_set = set()
    
    n = len(phrase)
    
    # Iterate over all possible start positions and lengths
    for i in range(n):
        current_length = 1
        while True:
            substring_end = i + current_length
            
            if substring_end > n:
                break
                
            end_idx = min(substring_end, n)
            
            current_substring = phrase[i:end_idx]
            
            # Check if this substring has been seen before (implies it appears at least twice)
            # Note: The problem asks for "nested substrings". In many contexts involving overlapping 
            # and efficiency, a common interpretation is finding patterns that repeat. 
            # If the requirement implies any substring appearing >= 2 times regardless of overlap structure,
            # we check existence in seen_substrings. However, strictly speaking, every string appears at least once.
            # The term "nested" here likely refers to substrings contained within others or simply repeated patterns.
            # Given the constraint "handling overlapping cases correctly", it implies finding all unique strings 
            # that occur multiple times (overlap allowed).
            
            if current_substring in seen_substrings:
                result_set.add(current_substring)
                
            seen_substrings.add(current_substring)
            current_length += 1
            
    return sorted(result_set, key=lambda x: (len(x), x))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_phrases = [
        "ababa",           # Expected nested substrings: 'a', 'b' appear multiple times; 'ab', 'ba' also repeat? 
                          # Actually in ababa: a(0), b(1), a(2), b(3), a(4). 
                          # Substrings:
                          # len 1: a (indices 0,2,4), b (indices 1,3) -> both nested.
                          # len 2: ab (0-1, 2-3), ba (1-2, 3-4) -> all repeat? 
                          # Wait, 'ab' is at 0 and 2. 'ba' is at 1 and 3. So yes.
                          # len 3: aba (0-2, 2-4). Yes.
                          # len 4: abab (0-3), baba (1-4). Yes.
        "aaaa",            # All substrings repeat or are part of the repetition chain.
        "abcde",           # No nested substrings as all unique except single chars if repeated? 
                          # Here no char repeats, so empty list expected for strict 'appears >= 2 times'.
                          # Wait, definition check: usually implies frequency > 1.
    ]

    sample_input = "ababa" 
    
    output_list = find_nested_substrings(sample_input)
    
    print(f"Input Phrase: {sample_input}")
    print("Nested Substrings (appearing more than once):")
    for item in output_list:
        print(item)