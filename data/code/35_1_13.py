def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Vowels include 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
    The function iterates through each character once for maximum efficiency.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowels found in the string.
    """
    vowel_set = set("aeiouAEIOU")
    count = 0
    
    # Single loop iteration over the string characters
    for char in text:
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_inputs = [
        "hello world",       # Expected output: 2 (e, o)
        "AEIOU",             # Expected output: 5
        "rhythm",            # Expected output: 0
        "aeiou AEIOU",       # Expected output: 10
        "",                  # Expected output: 0
    ]

    for test_string in sample_inputs:
        result = count_vowels(test_string)
        print(f"Input: '{test_string}' -> Vowel Count: {result}")