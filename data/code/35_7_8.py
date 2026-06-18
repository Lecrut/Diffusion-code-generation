import string

def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in the given text, case-insensitive.
    Vowels defined as 'a', 'e', 'i', 'o', 'u'.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowel characters found in the text.
    """
    vowels = set(string.ascii_lowercase + "AEIOU")  # Precompute for optimization
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_text_1 = "hello world"
    sample_text_2 = "aeiou AEIOU 123"
    
    result_1 = count_vowels(sample_text_1)
    print(f"The word 'hello world' has {result_1} vowel(s).")
    
    result_2 = count_vowels(sample_text_2)
    print(f"The text '{sample_text_2}' has {result_2} vowel(s).")