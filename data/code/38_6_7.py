import string

def count_letter_frequencies(text: str) -> dict[str, int]:
    """
    Count the frequency of each letter in the input text (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary mapping lowercase letters to their frequencies.
              Only includes letters that appear at least once.
    """
    # Initialize frequency counter for all alphabetic characters
    freq_counter = {char.lower(): 0 for char in string.ascii_lowercase}
    
    # Iterate through each character and update counts if it's a letter
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            freq_counter[lower_char] += 1
            
    return freq_counter

def report_high_frequency_letters(freq_map: dict[str, int]) -> list[tuple[str, int]]:
    """
    Return a sorted list of letters with frequency greater than one.
    
    Args:
        freq_map (dict): The dictionary returned by count_letter_frequencies.
        
    Returns:
        list: A list of tuples (letter, frequency), sorted alphabetically by letter.
              Only includes entries where frequency > 1.
    """
    high_freq_letters = [
        (char, count) 
        for char, count in freq_map.items() 
        if count > 1
    ]
    
    # Sort the list alphabetically by character
    return sorted(high_freq_letters, key=lambda x: x[0])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_text = "Hello World! This is a best-practice example."
    
    # Count frequencies and get high-frequency letters
    frequency_map = count_letter_frequencies(sample_text)
    result_letters = report_high_frequency_letters(frequency_map)
    
    # Print the results in a readable format
    print("Letter Frequencies (all):")
    for char, count in sorted(frequency_map.items()):
        if count > 0:
            print(f"  '{char}': {count}")
            
    print("\nLetters with frequency greater than one:")
    if result_letters:
        for letter, freq in result_letters:
            print(f"  '{letter}' appears {freq} times.")
    else:
        print("  No letters appear more than once.")