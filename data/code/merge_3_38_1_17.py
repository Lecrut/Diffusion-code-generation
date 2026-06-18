def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    The function is case-sensitive, treating 'A' and 'a' as distinct characters.
    Non-alphabetic characters are ignored from consideration but do not break processing.
    Only alphabetic characters (letters) are checked for repetition.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of letters appearing more than once in the string.
    """
    letter_counts = {}
    
    # Iterate over each character in the string
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    # Extract letters with count greater than 1
    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_input_1 = "hello world"
    result_1 = find_repeated_letters(sample_input_1)
    print(f"Input: '{sample_input_1}'")
    print(f"Repeated letters: {result_1}")

    sample_input_2 = "A man a plan a canal Panama"
    result_2 = find_repeated_letters(sample_input_2)
    print(f"\nInput: '{sample_input_2}'")
    print(f"Repeated letters: {result_2}")

    sample_input_3 = "abcde"
    result_3 = find_repeated_letters(sample_input_3)
    print(f"\nInput: '{sample_input_3}'")
    print(f"Repeated letters: {result_3}")