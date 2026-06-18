def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of lowercase alphabetic characters found twice or more in the sentence.
    """
    letter_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabetic letter to ensure we only process 'a'-'z' (case-insensitive)
        if char.isalpha():
            lower_char = char.lower()  # Normalize case
            if lower_char in letter_count:
                letter_count[lower_char] += 1
            else:
                letter_count[lower_char] = 1
                
    # Collect letters with a count greater than 1 into the result set
    repeated_letters = {letter for letter, count in letter_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentence: str = "Hello, World! This is an example of a sentence with repeated letters like 'e' and 'l'"
    
    # Process the hard-coded sample value to find repeated letters without user input
    result: set = find_repeated_letters(sample_sentence)
    
    if not result:
        print("No repeated letters found.")
    else:
        sorted_result = sorted(list(result))  # Sort for consistent output display
        print(f"Repeated letters in the sentence: {', '.join(sorted_result)}")