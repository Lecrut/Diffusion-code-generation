def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to count occurrences of each letter that appears more than once.
    
    Args:
        s (str): The input string containing letters and potentially other characters.
        
    Returns:
        dict[str, int]: A dictionary where keys are the repeated letters 
                        and values are their occurrence counts in the original string.
                        Only case-sensitive; only alphabetic characters are considered for repetition logic unless specified otherwise.
                        However, based on standard interpretation of "letters", we consider all alphabetic chars 'a'-'z'/'A'-'Z'.
    """
    count = {}

    # Iterate over each character in the string
    for char in s:
        if len(char) == 1 and (char.isalpha()):
            count[char] = count.get(char, 0) + 1

    # Filter to only include letters that are repeated (count > 1)
    result = {letter: freq for letter, freq in count.items() if freq > 1}

    return result

if __name__ == '__main__':
    sample_string = "A man, a plan, a canal: Panama"
    
    # Process the string and get the dictionary of repeated letters with counts
    frequency_dict = process_string(sample_string)

    print(frequency_dict)