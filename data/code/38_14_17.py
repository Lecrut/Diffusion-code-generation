def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to count occurrences of each letter that appears more than once.
    
    Args:
        s (str): The input string containing letters and potentially other characters.
        
    Returns:
        dict[str, int]: A dictionary where keys are repeated letters 
                        (case-sensitive) and values are their occurrence counts.
    """
    letter_counts = {}

    for char in s:
        if 'a' <= char.lower() <= 'z':  # Only consider alphabetic characters
            count = letter_counts.get(char, 0) + 1
            letter_counts[char] = count

    return {k: v for k, v in letter_counts.items() if v > 1}

if __name__ == '__main__':
    sample_string = "hello world"
    
    result_dict = process_string(sample_string)
    
    print(result_dict)