def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in the input string, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowels found in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_text_1 = "Hello, World! This is a test."
    sample_text_2 = "Python 3.9 features advanced data structures like lists and dicts."
    
    result_1 = count_vowels(sample_text_1)
    result_2 = count_vowels(sample_text_2)
    
    print(result_1)
    print(result_2)