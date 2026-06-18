def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of unique characters found multiple times, 
             including both uppercase and lowercase versions if they match case-insensitively,
             or individual letters if treated strictly by character identity unless specified otherwise.
    
    Note: This implementation treats 'A' and 'a' as distinct characters based on strict equality check in the dictionary keys,
          but groups them for display purposes only when needed (though here we return unique chars). 
          If case-insensitive matching is desired conceptually, one might normalize input first. 
          Here, to be precise about "letters" without assuming case sensitivity unless specified:
          We track counts per exact character instance. However, if 'A' and 'a' are considered the same letter type,
          we should probably group them. Let's assume standard English definition where A/a are the same letter 
          for simplicity in this context of "letters". So we normalize to lowercase before counting.
    """
    # Normalize sentence: keep only alphabetic characters and convert to lower case
    filtered_chars = [char.lower() for char in sentence if char.isalpha()]
    
    frequency_map = {}
    for char in filtered_chars:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    # Collect letters with count > 1
    repeated_letters = set(key for key, count in frequency_map.items() if count > 1)
    
    return repeated_letters

def main():
    """
    Main function to run the script.
    Uses hard-coded sample values as per requirements; no user input or interactive prompts are used.
    """
    # Sample sentences for testing without requiring external inputs
    samples = [
        "Hello, World!",
        "Python is great and Python works well",
        "The quick brown fox jumps over the lazy dog"
    ]

    print("Repeated letters in sample 1:", find_repeated_letters(samples[0]))
    print("Repeated letters in sample 2:", find_repeated_letters(samples[1]))
    print("Repeated letters in sample 3:", find_repeated_letters(samples[2]))

if __name__ == '__main__':
    main()