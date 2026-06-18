def process_string(input_str):
    """
    Processes a string to return three variations:
    1. The original string.
    2. Fully capitalized version.
    3. Title case (first letter of every word capitalized).
    
    Args:
        input_str (str): The input string to process.
        
    Returns:
        tuple: A tuple containing the three processed strings.
    """
    original = input_str
    
    # Fully capitalize using str.upper()
    fully_capitalized = original.upper()
    
    # Title case using built-in method which capitalizes first letter of each word
    title_case = original.title()
    
    return (original, fully_capitalized, title_case)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_input = "hello world"
    
    result = process_string(sample_input)
    
    original_str, cap_str, title_str = result
    
    print(original_str)
    print(cap_str)
    print(title_str)