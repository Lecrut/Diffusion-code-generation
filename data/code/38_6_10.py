import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the input text (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping letters to their frequencies. Only includes 
              alphabetic characters; other characters are ignored.
    """
    frequency_map = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if 'a' <= char <= 'z':  # Check if character is a letter
            frequency_map[char] = frequency_map.get(char, 0) + 1
            
    return frequency_map

def get_high_frequency_letters(frequency_map: dict[str, int]) -> list[str]:
    """
    Extract letters that appear more than once.
    
    Args:
        frequency_map (dict): The dictionary of letter frequencies.
        
    Returns:
        list: A sorted list of letters with a count greater than one.
    """
    high_freq_letters = [letter for letter, count in frequency_map.items() if count > 1]
    return sorted(high_freq_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_text = "Hello World! This is a best practice example."
    
    frequencies = count_letter_frequencies(sample_text)
    frequent_letters = get_high_frequency_letters(frequencies)
    
    print("Letter Frequencies:")
    for letter, count in sorted(frequencies.items()):
        print(f"  '{letter}': {count}")
        
    if not frequent_letters:
        print("\nNo letters appear more than once.")
    else:
        print(f"\nLetters appearing more than once (sorted):")
        for letter in frequent_letters:
            count = frequencies[letter]
            print(f"  '{letter}': {count}")