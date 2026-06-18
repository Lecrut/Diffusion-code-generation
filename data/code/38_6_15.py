import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter (a-z, A-Z) in the input text.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary mapping lowercase letters to their frequencies.
    """
    # Initialize a counter for all alphabetic characters
    frequency_map = {char.lower(): 0 for char in string.ascii_letters}

    # Iterate through each character and update the count if it is an alphabet letter
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            frequency_map[lower_char] += 1
            
    return frequency_map

def get_high_frequency_letters(frequency_map: dict[str, int]) -> list[str]:
    """
    Extract letters that have a frequency greater than one.
    
    Args:
        frequency_map (dict[str, int]): The dictionary of letter frequencies.
        
    Returns:
        list[str]: A sorted list of letters with frequency > 1.
    """
    return [letter for letter in string.ascii_lowercase if frequency_map[letter] > 1]

if __name__ == '__main__':
    # Hard-coded sample text without user input, network access, or file I/O
    sample_text = "Hello World! This is a best-practice Python solution. Hello again."

    count_result = count_letter_frequencies(sample_text)
    
    high_freq_letters = get_high_frequency_letters(count_result)
    
    # Printing results directly to stdout as per standard practice for this task type
    print("Letter Frequencies:")
    for letter in string.ascii_lowercase:
        if count_result[letter] > 0:
            print(f"{letter}: {count_result[letter]}")
            
    print("\nLetters with frequency greater than one:", high_freq_letters)