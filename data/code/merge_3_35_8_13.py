def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in the given text, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel occurrences.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_text_1 = "Hello, World! This is a test."
    sample_text_2 = "Python 3.9 features advanced data structures like lists and dicts."
    
    result_1 = count_vowels(sample_text_1)
    result_2 = count_vowels(sample_text_2)
    
    print(result_1)
    print(result_2)