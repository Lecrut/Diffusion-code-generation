def count_repeated_letters(text: str) -> dict:
    """
    Processes a string to find letters that appear more than once.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary where keys are repeated letters and values 
              are their occurrence counts in the original string.
    """
    letter_counts = {}
    
    # Iterate through each character in the string
    for char in text:
        if char.isalpha():  # Only consider alphabetic characters
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Filter to only include letters that appear more than once
    repeated_letters = {letter: count for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_repeated_letters(sample_string)
    print(result)