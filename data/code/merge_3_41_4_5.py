def process_string(input_str):
    """
    Takes a string input and returns three processed versions:
    1. The original string.
    2. The fully capitalized string.
    3. A title-cased version (first letter of every word capitalized).
    
    Args:
        input_str (str): The input string to process.
        
    Returns:
        tuple: A tuple containing the three processed strings.
    """
    original = input_str
    fully_capitalized = input_str.upper()
    title_cased = " ".join(word.capitalize() for word in input_str.split())
    
    return (original, fully_capitalized, title_cased)

if __name__ == '__main__':
    # Hard-coded sample value as per requirements. 
    # No user interaction or external dependencies are used here.
    sample_input = "hello world this is a test string"
    
    original_str, upper_str, title_str = process_string(sample_input)
    
    print(original_str)
    print(upper_str)
    print(title_str)