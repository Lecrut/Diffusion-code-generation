import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the input text (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping lowercase letters to their frequencies.
              Only includes keys that are alphabetic characters found in the text.
    """
    frequency_map = {}
    
    # Normalize text to lowercase and iterate over each character
    for char in text.lower():
        if 'a' <= char <= 'z':  # Check if it's an alphabet letter
            frequency_map[char] = frequency_map.get(char, 0) + 1
            
    return frequency_map

def get_high_frequency_letters(frequency_map: dict[str, int]) -> list[str]:
    """
    Extract letters that have a frequency greater than one.
    
    Args:
        frequency_map (dict): The dictionary returned by count_letter_frequencies.
        
    Returns:
        list: A sorted list of letters with frequency > 1.
    """
    high_freq_letters = [letter for letter, freq in frequency_map.items() if freq > 1]
    return sorted(high_freq_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_text = "Hello World! This is a best practice example for counting letters."
    
    frequencies = count_letter_frequencies(sample_text)
    high_frequency_chars = get_high_frequency_letters(frequencies)
    
    print("Letter Frequencies:")
    # Print all letter counts in sorted order by character
    for char, freq in sorted(frequencies.items()):
        print(f"  '{char}': {freq}")
        
    if not high_frequency_chars:
        print("\nNo letters have a frequency greater than one.")
    else:
        print(f"\nLetters with frequency > 1 (sorted):")
        for char in high_frequency_chars:
            count = frequencies[char]
            print(f"  '{char}': {count}")