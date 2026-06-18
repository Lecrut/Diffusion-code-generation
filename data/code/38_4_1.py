def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of characters that are repeated, converted to lowercase for consistency.
             Non-alphabetic characters and case sensitivity variations are handled by 
             considering only alphabetic letters in a case-insensitive manner.
    """
    letter_counts = {}

    # Iterate over each character in the sentence
    for char in sentence:
        if 'a' <= char.lower() <= 'z':  # Check if it's an alphabet letter
            lower_char = char.lower()
            
            # Increment count or initialize to 1
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1

    # Extract letters with a count greater than 1 into a set for uniqueness
    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python Programming is fun!",
        "A man a plan a canal Panama"
    ]

    for sentence in sample_sentences:
        result = find_repeated_letters(sentence)
        if len(result) > 0:
            print(f"In '{sentence}': Repeated letters are {sorted(list(result))}")
        else:
            print(f"No repeated letters found in '{sentence}'.")