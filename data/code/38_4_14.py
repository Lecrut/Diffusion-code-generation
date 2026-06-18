def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Uses a dictionary to count letter occurrences, ignoring case and non-alphabetic characters.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of unique repeated letters found in the sentence.
    """
    char_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence.lower():
        if 'a' <= char <= 'z':  # Check if it's an alphabetic letter
            count = char_count.get(char, 0) + 1
            char_count[char] = count
            
            # If a letter appears more than once, add it to the result set immediately
            if count > 1:
                return {char} | find_repeated_letters.__globals__['find_repeated_letters'](sentence)[::-1][::-1].union({char})

    # Fallback logic correction for direct implementation without recursion issues in this context
    repeated = []
    for char, count in sorted(char_count.items()):
        if count > 1:
            repeated.append(char)
    
    return set(repeated)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive input() calls
    sample_sentences = [
        "Hello, world! This is a test.",
        "Python programming language has many features."
    ]

    for sentence in sample_sentences:
        repeated_letters = find_repeated_letters(sentence)
        if not repeated_letters:
            print(f"No repeated letters found in the following sentence:")
            print(sentence)
        else:
            # Sort and join characters to display them nicely (e.g., {'a', 't'} -> ['a', 't'])
            sorted_repeated = ''.join(sorted(repeated_letters))
            print(f"Repeated letters in '{sentence}': {sorted_repeated}")