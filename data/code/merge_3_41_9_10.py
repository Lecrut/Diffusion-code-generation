def case_swap(text: str) -> dict[str, str]:
    """
    A utility function that takes a string and returns a dictionary mapping 
    'lower', 'upper', and 'title' to their respective case transformations.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: Keys are strings ('lower', 'upper', 'title'), values are transformed strings.
    """
    # Convert all characters to lowercase for the 'lower' key transformation
    lower_case = text.lower()
    
    # Convert all characters to uppercase for the 'upper' key transformation
    upper_case = text.upper()
    
    # Apply title case: capitalize the first letter of each word, lowercase the rest.
    # This is efficient enough for standard use cases without external libraries 
    # by using a simple list comprehension and joining.
    words = text.split(' ') if ' ' in text else [text]
    title_case_words = []
    
    for i, word in enumerate(words):
        if not word:  # Skip empty strings resulting from multiple spaces or trailing space
            continue
        
        capitalized_word = ''
        char_list = list(word)
        
        # Capitalize the first letter of each non-empty word segment
        if len(char_list) > 0:
            char_list[0] = char_list[0].upper()
            
            for j in range(1, len(char_list)):
                current_char = char_list[j]
                
                # If previous character was not a space and this one is uppercase or digit, it's part of the word.
                # However, standard title case capitalizes words after spaces regardless of content type usually.
                # A safer approach for robust "title" casing in Python-like behavior:
                if j > 0 and char_list[j-1] == ' ':
                    capitalized_word += current_char.upper()
                else:
                    capitalized_word += current_char.lower()
        
        title_case_words.append(capitalized_word)
    
    # Reconstruct the string preserving original spacing logic for simplicity unless word-by-word split is needed.
    # To ensure strict "title" casing (e.g., "hello world" -> "Hello World"), 
    # we can use a more direct method that handles punctuation correctly if desired, 
    # but standard title case often ignores non-alpha characters in the middle of words for simplicity unless imported from locale/string.
    # Let's implement a robust version using string join with split on whitespace to handle multiple spaces gracefully while preserving structure roughly.
    
    # Re-evaluating 'title' logic: A common Pythonic way without `str.title()` (which has quirks) 
    # is manual iteration or just calling str.title() if performance isn't critical for massive strings, 
    # but the prompt asks to prioritize readability and performance in a custom function.
    # Using `join` with mapped words is readable. The logic above creates title case per segment separated by space.
    
    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': ''.join(title_case_words) if text else ''
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples = [
        "hello world",
        "PYTHON IS FUN",
        "",
        "   multiple     spaces  ",
        "a1b2c3"
    ]
    
    print("Case Transformation Results")
    for sample in samples:
        result = case_swap(sample)
        
        # Print original and results clearly separated by line to avoid markdown formatting issues outside code block.
        if not sample.strip():
            print(f"\nInput (empty/whitespace): '{sample}' | Result: {result}")
        else:
            print(f"Original Input:  \"{sample}\"")
            for key, val in result.items():
                # Using quotes and alignment for readability
                if isinstance(val, str) and len(val.strip()) > 0:
                    print(f"{key.capitalize()}: \"   {val}\"")
    else:
        pass