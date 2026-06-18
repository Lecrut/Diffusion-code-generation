from collections import Counter

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Counts the frequency of each letter in the input string (case-insensitive).
    
    Args:
        text: The input string to analyze.
        
    Returns:
        A dictionary mapping lowercase letters to their frequencies.
    """
    # Filter out non-alphabetic characters and convert to lowercase
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    
    counter = Counter(filtered_text)
    return dict(counter)

def get_high_frequency_letters(freq_dict: dict[str, int]) -> list[tuple[str, int]]:
    """
    Returns a list of tuples containing letters with frequency greater than one.
    
    Args:
        freq_dict: Dictionary mapping letters to their frequencies.
        
    Returns:
        Sorted list of (letter, count) tuples where count > 1.
    """
    high_freq = [(char, count) for char, count in freq_dict.items() if count > 1]
    # Sort by letter first, then by frequency descending
    high_freq.sort(key=lambda x: (-x[1], x[0]))
    return high_freq

if __name__ == '__main__':
    sample_text = "Hello World! This is a best-practice example of counting letters."
    
    # Count frequencies
    letter_counts = count_letter_frequencies(sample_text)
    
    print("Letter Frequencies:")
    for char, freq in sorted(letter_counts.items()):
        if freq > 0:
            print(f"{char}: {freq}")
        
    # Report letters with frequency greater than one
    high_freq_letters = get_high_frequency_letters(letter_counts)
    
    print("\nLetters with Frequency Greater Than One:")
    for char, count in high_freq_letters:
        print(f"'{char}': {count} times")