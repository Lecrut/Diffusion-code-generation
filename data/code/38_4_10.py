def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Uses a dictionary to count occurrences of each letter, ignoring case and non-alphabetic characters.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set containing the unique repeated letters found in the sentence.
    """
    char_count = {}
    
    # Iterate over each character in the sentence
    for char in sentence.lower():
        if 'a' <= char <= 'z':  # Check if it's an alphabetic letter
            count = char_count.get(char, 0) + 1
            char_count[char] = count
            
    # Extract letters with a count greater than one
    repeated_letters = {letter for letter, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentences = [
        "Hello World!",
        "Python is great and Python works well",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    for sentence in sample_sentences:
        result = find_repeated_letters(sentence)
        if not result:
            print(f"No repeated letters found in '{sentence}'")
        else:
            sorted_result = "".join(sorted(result))
            print(f"'{sorted_result}' are the repeated letters in '{sentence}'")