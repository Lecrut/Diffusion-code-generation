import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter (a-z, A-Z) in the input text.
    
    Args:
        text: The input string to analyze.
        
    Returns:
        A dictionary mapping lowercase letters to their occurrence counts.
    """
    frequencies = {}
    for char in text.lower():
        if 'a' <= char <= 'z':
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def get_high_frequency_letters(frequencies: dict[str, int]) -> list[str]:
    """
    Extract letters that appear more than once.
    
    Args:
        frequencies: Dictionary of letter counts from count_letter_frequencies.
        
    Returns:
        A sorted list of letters with frequency > 1.
    """
    high_freq = [letter for letter, count in frequencies.items() if count > 1]
    return sorted(high_freq)

if __name__ == '__main__':
    # Hard-coded sample string without user input or external dependencies
    sample_text = "Hello World! This is a best practice example."

    freq_map = count_letter_frequencies(sample_text)
    high_freq_letters = get_high_frequency_letters(freq_map)

    print("Letter frequencies:")
    for letter, count in sorted(freq_map.items()):
        print(f"  '{letter}': {count}")

    if not high_freq_letters:
        print("\nNo letters appear more than once.")
    else:
        print(f"\nLetters with frequency > 1 (sorted):")
        for letter in high_freq_letters:
            count = freq_map[letter]
            print(f"  '{letter}': {count}")