def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Vowels considered include 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    if not isinstance(text, str):
        return 0
    
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    text_lower = text.lower()
    
    # Single loop iteration for maximum efficiency
    count = 0
    for char in text_lower:
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "AEIOUaeiou",
        "",
        "rhythm"
    ]
    
    for test_input in sample_strings:
        result = count_vowels(test_input)
        print(f"'{test_input}' -> {result}")