def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in a given string,
    handling both uppercase and lowercase letters using list comprehension.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel characters found.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "AEIOU",
        "Python Programming: A Vowel Adventure.",
        "",
        "b"  # String with no vowels
    ]

    for test_input in sample_strings:
        result = count_vowels(test_input)
        print(f"'{test_input}' -> {result} vowels")