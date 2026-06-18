import string

def find_repeated_letters(sentence):
    """
    Identifies letters that appear more than once in a given sentence using 
    efficient data structures (sets). The function ignores case, spaces, and non-alphabetic characters.

    Args:
        sentence (str): Input text to analyze.

    Returns:
        set: A set of unique uppercase letters found multiple times in the input.
    """
    seen_letters = {}  # Dictionary to count occurrences as we iterate once
    
    # Iterate through each character in the string efficiently
    for char in sentence.lower():
        if 'a' <= char <= 'z':  # Check if it is a lowercase alphabet letter
            seen_letters[char] += 1
            
    # Create another set from keys to filter only those with count > 1, 
    # then convert back and uppercase them as the result.
    repeated = {letter for letter in seen_letters.keys() if seen_letters[letter] > 1}
    
    return [char.upper() for char in sorted(repeated)]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required.
    test_sentence = "Hello, World! Hello Python."
    
    result_letters = find_repeated_letters(test_sentence)
    
    print("Repeated letters in the sentence:", ", ".join(result_letters))