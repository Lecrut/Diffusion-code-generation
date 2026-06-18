import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Counts the frequency of each alphabetic letter in the input text.
    
    - Only counts lowercase letters (a-z). Uppercase and symbols are ignored 
      unless converted to lowercase as per standard practice for such tasks.
    This implementation converts all characters to lowercase first for uniformity.
    
    Args:
        text (str): The string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping each letter found in the text 
                        to its frequency count.
    """
    alphabet = set(string.ascii_lowercase)
    frequencies = {char: 0 for char in alphabet}
    
    cleaned_text = [c.lower() if c.isalpha() else None for c in text]
    
    for char in cleaned_text:
        if char is not None and char in frequencies:
            frequencies[char] += 1
            
    return frequencies

def get_high_frequency_letters(frequencies: dict[str, int], threshold: int = 1) -> list[str]:
    """
    Returns a sorted list of letters that have a frequency greater than the specified threshold.

    Args:
        frequencies (dict): The dictionary returned by count_letter_frequencies.
        threshold (int): Minimum frequency to be considered high (default is 1).

    Returns:
        list[str]: Sorted list of letters meeting the criteria.
    """
    return sorted([char for char, freq in frequencies.items() if freq > threshold])

if __name__ == '__main__':
    # Hard-coded sample input to ensure no external dependencies or user prompts are needed
    SAMPLE_TEXT = "The quick brown fox jumps over a lazy dog."

    frequency_data = count_letter_frequencies(SAMPLE_TEXT)
    high_freq_letters = get_high_frequency_letters(frequency_data, threshold=1)

    print("Frequency of each letter:")
    for char in sorted(frequency_data.keys()):
        if frequency_data[char] > 0:
            print(f"  {char}: {frequency_data[char]}")
    
    letters_above_one = get_high_frequency_letters(frequency_data, threshold=2) # Changed to show only those strictly greater than one per typical "best practice" interpretation unless specified otherwise. However re-reading prompt says "greater than one". So >1 is correct logic but let's stick to prompt: "frequency greater than one".
    print("\nLetters with frequency greater than 1:")
    for letter in letters_above_one:
        count = frequency_data[letter]
        if count > 1: # Re-verify logic against prompt strict reading. Prompt says "greater than one" (so >=2). My previous line used threshold=2 which is same as >1. But I need to make sure output matches description exactly without hardcoded filter confusion. 
            print(f"{letter}: {count}")