def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, 
    ignoring case sensitivity and treating non-alphabetic characters as ignored.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel occurrences.
    """
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    sample_inputs = [
        "Hello, World!",       # Expected: 2 (e, o)
        "Python Programming",  # Expected: 4 (y is not counted here per standard definition unless specified otherwise; i, o, a, e -> actually 'o', 'r' no. Let's recount: P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g. Vowels: o, o, a, i = 4)
        "aeiouAEIOU",          # Expected: 10
        "",                    # Expected: 0
        "Rhythm is Syzgy!",    # Expected: 2 (y in Rhy... wait 'y' is not standard. Let's stick to a,e,i,o,u only). Actually no vowels here if y is excluded? r-h-y-t-h-m- -i-s- -s-y-z-g-y-. Only 'i'. So expected 1.)
    ]

    for test_string in sample_inputs:
        # Note on Sample Inputs logic based on strict a-e-i-o-u definition:
        # "Hello, World!" -> e, o (2)
        # "Python Programming" -> o, o, a, i (4). 'y' is excluded.
        # "aeiouAEIOU" -> 10
        # "" -> 0
        # "Rhythm is Syzgy!" -> Only 'i'. So expected 1.
        
        count = count_vowels(test_string)
        print(f"Input: '{test_string}' => Count: {count}")