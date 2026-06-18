"""
Best-practice Python solution to count letter frequency in a string
and report letters with frequency greater than one.

This module demonstrates clean, readable coding practices including:
- Clear function separation (count_letters, get_high_frequency)
- Docstrings for documentation
- Type hints
- Comprehensive error handling where appropriate
"""

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the given text.

    Only alphabetic characters are counted (case-insensitive). 
    Non-alphabetic characters and whitespace are ignored.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary mapping lowercase letters to their counts.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type but got {type(text).__name__}")

    frequencies = {}
    
    # Normalize text and iterate through characters
    for char in text.lower():
        if 'a' <= char <= 'z':  # Check only alphabetic characters
            counts_char = frequencies.get(char, 0) + 1
            frequencies[char] = counts_char
            
    return frequencies

def get_high_frequency_letters(frequencies: dict[str, int]) -> list[tuple[str, int]]:
    """
    Extract letters with a frequency greater than one.

    Args:
        frequencies (dict[str, int]): The letter count dictionary from the main function.

    Returns:
        list[tuple[str, int]]: A sorted list of tuples containing 
                               (letter, count) for letters appearing more than once.
                               
    Raises:
        TypeError: If input is not a valid frequency dictionary.
        
    Note: Results are sorted alphabetically by letter for consistent output.
    """
    if not isinstance(frequencies, dict):
        raise TypeError("Expected dictionary type but got {type(frequencies).__name__}")

    high_freq = [
        (letter, count) 
        for letter, count in frequencies.items() 
        if count > 1
    ]
    
    # Sort alphabetically by the first element of each tuple (the letter)
    return sorted(high_freq, key=lambda x: x[0])

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed
    
    # Sample 1: A mixed string with various letters and punctuation
    sample_string_1 = "The quick brown fox jumps over the lazy dog!"
    
    # Sample 2: A sentence repeated twice for obvious duplicates
    sample_string_2 = "Hello world Hello World hello WORLD"

    print("=" * 50)
    print("Letter Frequency Analysis")
    print("=" * 50)
    
    samples_to_analyze = [sample_string_1, sample_string_2]
    
    for i, text in enumerate(samples_to_analyze, 1):
        print(f"\n--- Sample {i} ---\nInput: \"{text}\"")

        try:
            # Step 1: Count frequencies
            counts = count_letter_frequencies(text)
            
            if not counts:
                print("No letters found.")
                continue
                
            # Display full frequency map (optional, for clarity)
            sorted_counts = dict(sorted(counts.items()))
            print("\nAll Letter Frequencies:")
            for letter in sorted_counts.keys():
                count = sorted_counts[letter]
                marker = ">>>" if count > 1 else ""
                print(f"  '{letter}': {count}{marker}")

            # Step 2: Get and report high frequency letters (frequency > 1)
            high_freq_letters = get_high_frequency_letters(counts)
            
            print("\nLetters with Frequency Greater Than One:")
            if not high_freq_letters:
                print("  None found.")
            else:
                for letter, count in high_freq_letters:
                    print(f"  '{letter}': {count}")

        except TypeError as e:
            print(f"\nError processing sample {i}: {e}")