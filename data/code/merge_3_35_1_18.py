def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a string using a single loop.
    
    Vowels considered include both uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Single loop iteration to traverse and check each character efficiency-wise
    count = 0
    for char in text:
        if char.lower() in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "aeiouAEIOU", "", "Python Programming"]
    
    results = []
    for test_case in sample_strings:
        result = count_vowels(test_case)
        # f-string formatting is valid here without requiring user input or CLI args
        print(f"Input: \"{test_case}\" -> Vowel Count: {result}")