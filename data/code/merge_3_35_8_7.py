import re

def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in the input text, ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The total count of vowel occurrences ('a', 'e', 'i', 'o', 'u' case-insensitive).
    """
    vowels = set("aeiouAEIOU")
    
    # Use regex or manual iteration; here using generator expression for efficiency and clarity.
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test case with some numbers 12345 and symbols @#$%^&*()."
    
    result = count_vowels(sample_text)
    
    print(result)