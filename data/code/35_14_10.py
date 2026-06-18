import argparse

def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowels found in the string.
    """
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count total vowels in a provided sentence.')
    
    # Using optional arguments to avoid interactive prompts as per constraints.
    input_text_arg = parser.add_argument('input_text', nargs='?', default=None, help='The word or sentence to analyze (optional).')
    
    args = parser.parse_args()
    
    if args.input_text is not None:
        user_input = args.input_text
    else:
        # Hard-coded sample value as required by the task logic for non-interactive runs.
        user_input = "Hello, World!"
    
    result = count_vowels(user_input)
    print(f"The total vowel count in '{user_input}' is {result}.")