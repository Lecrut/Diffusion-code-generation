import string

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Uses a dictionary to count occurrences of each character, filtering out 
    non-alphabetic characters and case sensitivity by converting input to lowercase.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        set: A set containing unique letters that are repeated in the sentence.
    """
    char_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence.lower():
        if char.isalpha():  # Ensure only alphabetic characters are counted
            char_count[char] = char_count.get(char, 0) + 1

    # Extract letters with a count greater than one and return as a set
    repeated_letters = {letter for letter, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence. Aaa."
    result = find_repeated_letters(sample_sentence)
    print(f"Repeated letters: {sorted(result)}")