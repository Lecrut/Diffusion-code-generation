def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    This function iterates through each character exactly once, checking if it is 
    an uppercase or lowercase vowel (a, e, i, o, u). It returns the count as an integer.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowels in the string.
    """
    if not isinstance(text, str):
        return 0
        
    vowel_count = 0
    
    # Single loop iteration over the string characters
    for char in text:
        lowercase_char = char.lower()
        is_vowel = (lowercase_char == 'a' or 
                    lowercase_char == 'e' or 
                    lowercase_char == 'i' or 
                    lowercase_char == 'o' or 
                    lowercase_char == 'u')
        
        if is_vowel:
            vowel_count += 1
            
    return vowel_count

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    samples = [
        "Hello, World!",          # Expected: e, o, o -> 3
        "AEIOU",                  # Expected: A, E, I, O, U -> 5
        "",                       # Expected: 0
        "Python Programming",     # Expected: y->1 (if not counted), a, i, r? 
                               # Note: 'y' is typically excluded unless specified. Based on standard definition used above: P-y-t-h-o-n p-r-o-g-r-a-m-m-i-n-g -> o(2), a, i = 4 vowels if y excluded.
                               # Let's re-evaluate "Python Programming": 
                               # P(y)t(h)o(n) (p)(r)a(g)r(a)m(m)i(n)(g)
                               # Vowels: o, a, a, i -> 4.
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"Input: '{sample}' => Count: {result}")