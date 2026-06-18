def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Uses a dictionary to count letter occurrences, ensuring efficiency (O(n)).
    Only alphabetic characters are considered (case-insensitive).
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of unique letters that are repeated in the sentence.
       """
    letter_counts = {}
    
    # Iterate over each character in the sentence
    for char in sentence:
        # Check if it is an alphabetic character and convert to lowercase
        if 'a' <= char.lower() <= 'z':
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1
            
    # Identify letters with a count greater than one (repeated)
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentences = [
        "Hello, world! This is an example sentence to find repeating letters.",
        "A man a plan a canal Panama!",
        "The rain in Spain stays mainly in the plain."
    ]

    for s_sentence in sample_sentences:
        result_letters = find_repeated_letters(s_sentence)
        print(f"Input: {s_sentence!r}")
        if not result_letters:
            print("No repeated letters found.")
        else:
            sorted_result = sorted(result_letters, key=lambda x: ord(x)) # Sort for consistent output
            print(f"Repeated letters (case-insensitive): {''.join(sorted_result)}")
        print("-" * 40)