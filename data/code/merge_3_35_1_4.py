def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in the input string.
    
    This function uses a single loop to iterate through each character,
    checking if it is an uppercase or lowercase vowel (a, e, i, o, u).

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowels found in the string.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    
    # Single loop iteration for maximum efficiency
    for char in text:
        if char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "AEIOU",
        "",
        "Python Programming"
    ]
    
    for test_str in sample_strings:
        result = count_vowels(test_str)
        print(f"'{test_str}' -> {result}")