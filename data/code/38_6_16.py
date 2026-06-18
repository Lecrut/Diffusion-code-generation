import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in a given text (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary mapping lowercase letters to their frequencies.
    """
    # Initialize counters for all alphabetic characters
    frequency_map = {char.lower(): 0 for char in string.ascii_lowercase}
    
    # Iterate through the text and count occurrences of each letter
    for char in text:
        if char.isalpha():
            frequency_map[char.lower()] += 1
            
    return frequency_map

def get_letters_with_frequency_greater_than_one(frequency_map: dict[str, int]) -> list[str]:
    """
    Extract letters that appear more than once from the frequency map.
    
    Args:
        frequency_map (dict[str, int]): Dictionary of letter frequencies.
        
    Returns:
        list[str]: Sorted list of letters with a count greater than 1.
    """
    return sorted([letter for letter, count in frequency_map.items() if count > 1])

if __name__ == '__main__':
    # Hard-coded sample string containing various characters including repeated letters
    sample_text = "Hello, World! This is a best-practice example. Python makes it easy."
    
    # Count frequencies and get result
    letter_counts = count_letter_frequencies(sample_text)
    frequent_letters = get_letters_with_frequency_greater_than_one(letter_counts)
    
    print(f"Letter frequency analysis for: '{sample_text}'")
    print("-" * 40)
    print("Letters with frequency > 1:")
    for letter in frequent_letters:
        count = letter_counts[letter]
        print(f"{letter}: {count}")