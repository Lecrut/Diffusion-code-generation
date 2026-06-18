def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function considers both uppercase and lowercase letters as distinct unless 
    specified otherwise; however, based on standard interpretation for such tasks, 
    we treat 'A' and 'a' as different characters. If case-insensitive matching is 
    desired, it can be adjusted here. For this implementation, exact character match 
    (case-sensitive) is used to find duplicates.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of characters that appear more than once in the string.
    """
    char_count = {}
    for char in text:
        if char.isalpha():  # Only consider alphabetic letters
            char_count[char] = char_count.get(char, 0) + 1
    
    repeated_letters = {char for char, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_input_1 = "hello world"
    sample_input_2 = "A man a plan a canal Panama"
    sample_input_3 = "abcdefg"
    
    result_1 = find_repeated_letters(sample_input_1)
    print(f"Input: '{sample_input_1}'")
    print(f"Repeated letters: {result_1}")
    
    result_2 = find_repeated_letters(sample_input_2)
    print(f"\nInput: '{sample_input_2}'")
    print(f"Repeated letters: {result_2}")
    
    result_3 = find_repeated_letters(sample_input_3)
    print(f"\nInput: '{sample_input_3}'")
    print(f"Repeated letters: {result_3}")