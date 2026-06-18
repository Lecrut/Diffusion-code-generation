def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowels found in the string.
    """
    if not isinstance(text, str):
        return 0

    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert text to lowercase and filter for alphabetic characters only
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    
    count = sum(1 for vowel_char in filtered_text if vowel_char in vowels)
    
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access
    samples = [
        "Hello, World!",           # Expected: 2 (e, o)
        "aeiouAEIOU123",          # Expected: 8 (all letters are vowels)
        "rhythm! @... ",          # Expected: 0 (no vowels as 'y' is ignored here for simplicity in this basic logic if not specified otherwise; strictly a,e,i,o,u only)
        "Python Programming",      # Expected: 3 (o, o, i - wait: P-y-t-h-o-n-P-r-o-g-r-a-m-m-i-n-g -> o, o, a, i = 4. Let's re-evaluate manually.)
                                  # Python: y,t,h,o,n (1) 
                                  # PrograMming: r,o,g,r,a,m,i,n,g (2 more? no, 'o' is vowel, 'a', 'i'. So o, a, i = 3 total in Prog...)
                                  # Total: o (Python), o (Prog), a (Program), i (Programming) -> 4 vowels.
    ]

    for sample_text in samples:
        result = count_vowels(sample_text)
        print(f"Input: '{sample_text}'")
        print(f"Vowel Count: {result}")