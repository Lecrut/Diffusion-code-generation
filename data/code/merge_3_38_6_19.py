def count_letter_frequency(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in a string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary where keys are letters and values 
                        are their respective counts (case-insensitive).
    """
    char_counts = {}
    
    # Iterate over each character in the text
    for char in text.lower():  # Convert to lowercase for case-insensitivity
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are counted
            char_counts[char] = char_counts.get(char, 0) + 1
            
    return char_counts

def report_high_frequency_letters(frequency_dict: dict[str, int]) -> list[tuple]:
    """
    Return a sorted list of tuples containing letters with frequency greater than one.
    
    Args:
        frequency_dict (dict[str, int]): Dictionary mapping letters to their counts.
        
    Returns:
        list[tuple]: List of tuples (letter, count) where count > 1, 
                    sorted alphabetically by letter.
    """
    high_freq_letters = [
        (char, count) for char, count in frequency_dict.items() if count > 1
    ]
    
    return sorted(high_freq_letters, key=lambda x: x[0])

if __name__ == '__main__':
    # Hard-coded sample string with no user input or external dependencies
    sample_text = "Hello World! This is a Python example."
    
    # Count frequencies of each letter in the sample text
    frequency_map = count_letter_frequency(sample_text)
    
    print("Letter Frequencies:")
    for char, freq in sorted(frequency_map.items()):
        if freq > 1:
            print(f"{char}: {freq}")

    print("\nLetters with Frequency Greater Than One (Sorted):")
    high_freq_result = report_high_frequency_letters(frequency_map)
    
    # Display the result as a list of tuples for clarity
    print(high_freq_result)