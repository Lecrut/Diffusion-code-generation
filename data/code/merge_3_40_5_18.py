def get_first_letters(word_string):
    """
    Takes a string as input and returns a dictionary where keys are words 
    (excluding punctuation) and values are their respective first letters.
    
    Args:
        word_string (str): The input string containing words and potentially punctuation.
        
    Returns:
        dict: A dictionary mapping each clean word to its first letter in uppercase.
    """
    result = {}
    
    # Split the string into tokens based on whitespace
    for token in word_string.split():
        # Clean the token by stripping leading/trailing punctuation and converting to lowercase for consistency during split
        cleaned_token = ''.join(char.lower() if char.isalpha() else '' 
                                for char in token)
        
        if not cleaned_token:
            continue
            
        first_letter = None
        for letter in cleaned_token:
            # Ensure we are only dealing with alphabetic characters to find the true first letter
            if letter.isalpha():
                first_letter = letter.upper()
                break
        
        word_key = ''.join(char.lower() for char in cleaned_token)
        
        result[word_key] = first_letter
    
    return result

if __name__ == '__main__':
    sample_input = "Hello, World! How are you? Python is great. Great Python!"
    
    output_dict = get_first_letters(sample_input)
    
    print("Input:", repr(sample_input))
    print("\nOutput Dictionary:")
    for word, letter in sorted(output_dict.items()):
        print(f"  '{word}': {letter}")