def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    if not isinstance(text, str):
        return 0
    
    vowel_set = set("aeiouAEIOU")
    count = 0
    
    for char in text:
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello, World!",
        "AEIOU",
        "",
        "Python Programming",
        "aeiou" * 10
    ]

    for test_string in samples:
        result = count_vowels(test_string)
        print(f"'{test_string}' -> {result} vowels")