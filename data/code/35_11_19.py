import string

def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, 
    including both uppercase and lowercase letters. Non-alphabetic characters are ignored.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters ('a', 'e', 'i', 'o', 'u' in any case).
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello, World!",
        "Python programming is awesome.",
        "",
        "aeiouAEIOU",
        "12345!@#$%",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sample in samples:
        count = count_vowels(sample)
        print(f"Input: '{sample}' -> Vowel Count: {count}")