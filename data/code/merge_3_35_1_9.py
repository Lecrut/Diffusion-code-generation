def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string.
    The function handles both uppercase and lowercase letters efficiently 
    using a single loop with set membership checking.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text if char.lower() in vowel_set)

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [
        "Hello, World!",  # Expected: 2 (e, o)
        "AEIOUaeiou",     # Expected: 10
        "",               # Expected: 0
        "Rhythm is yesteryear.",  # Expected: 6 (y, i, e, a - note: 'y' usually not counted here unless specified; this implementation counts only a,e,i,o,u) -> Correction based on strict definition: e, o, a, e -> 4. But let's re-evaluate sample carefully later if needed. Actually y is NOT in {a,e,i,o,u}. So Rhythm (y,h,r,t,h,m), is(i,s,y,e,s)t(y,e,a,r). Vowels: i, e, e, a = 4.)
    ]

    for test_str in samples:
        result = count_vowels(test_str)
        print(f"'{test_str}' -> {result}")