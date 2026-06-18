import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the input text (case-insensitive).
    
    Args:
        text: The input string to analyze.
        
    Returns:
        A dictionary mapping lowercase letters to their frequencies.
    """
    # Initialize a counter for all alphabetic characters
    freq = {char.lower(): 0 for char in string.ascii_lowercase}

    # Iterate through the text and update counts only for alphabetic characters
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            freq[lower_char] += 1
            
    return freq

def get_high_frequency_letters(freq_map: dict[str, int]) -> list[str]:
    """
    Extract letters that appear more than once from the frequency map.
    
    Args:
        freq_map: Dictionary of letter frequencies.
        
    Returns:
        A sorted list of letters with a count greater than 1.
    """
    high_freq = [letter for letter, count in freq_map.items() if count > 1]
    return sorted(high_freq)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_text = "Hello World! This is a best practice example."

    # Count frequencies
    letter_counts = count_letter_frequencies(sample_text)

    # Identify letters with frequency > 1
    frequent_letters = get_high_frequency_letters(letter_counts)

    print(f"Letter Frequencies: {letter_counts}")
    print(f"\nLetters appearing more than once (sorted): {frequent_letters}")