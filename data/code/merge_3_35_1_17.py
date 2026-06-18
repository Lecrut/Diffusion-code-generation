def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel characters ('a', 'e', 'i', 'o', 'u').
    """
    if not isinstance(text, str):
        return 0
    
    vowels = {'a': True, 'A': True, 'e': True, 'E': True, 
              'i': True, 'I': True, 'o': True, 'O': True, 
              'u': True, 'U': True}
    
    count = 0
    for char in text:
        if vowels.get(char):
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello, World!",      # Expected: 2 (e, o)
        "AEIOU",              # Expected: 5
        "",                   # Expected: 0
        "rhythm is it?",     # Expected: 1 (i - note: 'y' and 'o' excluded based on standard definition used here unless specified otherwise; actually 'o' in rhythm? No, r-h-y-t-h-m. i in is. o in ? none. u in ? none. Wait: "rhythm" has no vowels if y isn't counted strictly. "is" has i. "?" none. Total 1.)
        # Correction on sample logic for clarity and robustness based on strict aeiou only:
        "Beautiful Day!",     # Expected: 4 (e, u, i - wait 'a', 'u', 'i'. B-e-a-u-t-i-f-u-l-! -> e,a,u,i,u = 5)
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' contains {result} vowels.")