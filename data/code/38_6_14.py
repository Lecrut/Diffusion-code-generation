import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the input text (case-insensitive).
    
    Only alphabetic characters are considered; digits and spaces are ignored.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary mapping lowercase letters to their frequencies.
    """
    # Normalize the text to lowercase for case-insensitive counting
    normalized_text = text.lower()
    
    frequency_map = {}
    
    for char in normalized_text:
        if char.isalpha():  # Ensure we only count alphabetic characters
            if char not in frequency_map:
                frequency_map[char] = 0
            frequency_map[char] += 1
            
    return frequency_map

def get_letters_with_frequency_greater_than_one(frequency_map: dict[str, int]) -> list[str]:
    """
    Extract letters that appear more than once from the frequency map.
    
    Args:
        frequency_map (dict[str, int]): The dictionary of letter frequencies.
        
    Returns:
        list[str]: A sorted list of letters with a count greater than 1.
    """
    high_frequency_letters = [letter for letter, count in frequency_map.items() if count > 1]
    
    # Sort the result alphabetically to ensure consistent output order
    return sorted(high_frequency_letters)

if __name__ == '__main__':
    sample_text = "Hello World! This is a Python best practice example."
    
    frequencies = count_letter_frequencies(sample_text)
    frequent_letters = get_letters_with_frequency_greater_than_one(frequencies)
    
    print("Letter Frequencies:")
    for letter, count in sorted(frequencies.items()):
        if count > 0:
            print(f"{letter}: {count}")
            
    print("\nLetters with frequency greater than one:", frequent_letters)