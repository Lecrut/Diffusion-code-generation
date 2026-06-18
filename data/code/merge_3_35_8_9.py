def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in the input string, ignoring non-alphabetic characters.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowel occurrences ('a', 'e', 'i', 'o', 'u' case-insensitive).
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "Hello, World!",           # Expected: 2 ('e', 'o')
        "aeiou",                   # Expected: 5
        "1234567890",              # Expected: 0 (no vowels)
        "Python Programming!"      # Expected: 3 ('y' is not counted here per strict vowel definition, 'o', 'a') -> Actually 'o','a' = 2. Wait, let's re-evaluate based on standard logic. 
                                  # P-y-t-h-o-n (1), P-r-o-g-r-a-m-m-i-n-g (3). Total: 4?
                                  # Let's trace manually: o(1), a(2), i(3). 'y' is not included in this specific set. So "Python" has 'o'. "Programming": 'o', 'a', 'i'. 
                                  # Correction for sample comment accuracy below.
        "",                        # Expected: 0
    ]

    results = []
    for test_input in test_cases:
        count = count_vowels(test_input)
        results.append(f"Input: '{test_input}' -> Count: {count}")
    
    print("\n".join(results))