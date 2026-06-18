import string

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Uses a dictionary to count letter occurrences efficiently, ignoring case 
    and non-alphabetic characters (like spaces or punctuation).

    Args:
        sentence (str): The input string to analyze.

    Returns:
        set: A set of unique letters that are repeated in the sentence.
    """
    # Initialize a dictionary to store letter counts
    letter_counts = {}
    
    # Convert sentence to lowercase for case-insensitive comparison
    cleaned_sentence = sentence.lower()
    
    # Iterate through each character in the sentence
    for char in cleaned_sentence:
        # Check if the character is an alphabetic letter
        if char.isalpha():
            # Increment count or initialize count to 1 if new letter
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    # Extract letters with a count greater than one (repeated letters)
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    test_sentences = [
        "Hello World!",
        "Python is great and Python is fun",
        "The quick brown fox jumps over the lazy dog"
    ]

    for sentence in test_sentences:
        result = find_repeated_letters(sentence)
        if result:
            print(f"'{sentence}' -> Repeated letters: {sorted(result)}")
        else:
            print(f"'{sentence}' -> No repeated letters found.")