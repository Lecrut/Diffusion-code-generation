def find_repeated_letters(sentence):
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Uses a dictionary to count occurrences of each character, filtering out non-letter characters.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        list: A sorted list of unique repeated letters found in the sentence.
    """
    letter_counts = {}

    for char in sentence.lower():
        # Check if character is an alphabetic letter
        if 'a' <= char <= 'z':
            count = letter_counts.get(char, 0) + 1
            letter_counts[char] = count
    
    repeated_letters = [char for char, count in letter_counts.items() if count > 1]

    # Sort the result to ensure consistent output order regardless of input character appearance
    return sorted(repeated_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction or files)
    sample_sents = [
        "Hello, world! This is a test for repeated letters.",
        "Python programming involves loops and functions often used together."
    ]

    print("Repeated Letters Analysis:")
    print("-" * 30)

    for sentence in sample_sents:
        result = find_repeated_letters(sentence)
        
        # Display the original sentence (cleaned of punctuation/numbers conceptually, but keeping letters only logic applied internally)
        clean_sentence = "".join(c.lower() if 'a' <= c <= 'z' else '' for c in sentence)
        
        print(f"Input: '{sentence}'")
        print(f"Cleaned Letters (lowercase): '{clean_sentence}'")
        print(f"Repeated letters found: {result}")
        print("-" * 30)