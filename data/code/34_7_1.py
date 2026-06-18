def capitalize_words(text: str) -> str:
    """
    Decorator-like function that capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Split the string into words based on whitespace and punctuation (simplified)
    import re
    
    def process_word(word):
        return word[0].upper() + word[1:] if len(word) > 0 else ""
    
    # Use regex to split by non-alphabetic characters, filter out empty strings, then map the function back together
    words = [process_word(w) for w in re.findall(r'\S+', text)]
    return " ".join(words)

def capitalize_words_decorator(func):
    """Decorator that applies capitalization logic before calling a string-processing function."""
    def wrapper(text: str) -> str:
        processed_text = func(text)
        if not isinstance(processed_text, str):
            raise TypeError("Function must return a string.")
        
        # Capitalize first letter of every word in the result
        words = re.split(r'[\s_]+', processed_text.strip())  # Split by whitespace and underscore for simplicity
        
        capitalized_words = []
        if not any(words):  # Handle empty list case
            return ""
            
        current_word_capitalized = True
        final_words = []
        
        for word in words:
            new_word = capitalize_words(word)
            final_words.append(new_word)
        
        return " ".join(final_words).strip()

    return wrapper

# Example usage without external dependencies or user input
if __name__ == '__main__':
    # Define a sample function to demonstrate the decorator's effect on output strings
    def process_text(s):
        s = str(s)
        if not s:
            return "empty"
        
        # Simple transformation before capitalization for demonstration purposes (e.g., converting numbers to words isn't needed here, just processing text structure)
        parts = re.split(r'[\s]+', s.strip())
        result_parts = []
        for part in parts:
            if len(part) > 0 and not any(c.isalpha() for c in part):
                continue # Skip non-alphabetic tokens like numbers or symbols alone
            
            # Apply the decorator logic manually here to simulate usage since we are wrapping a function call directly
            new_part = capitalize_words(part)
            result_parts.append(new_part)
            
        return " ".join(result_parts).strip()

    @capitalize_words_decorator
    def apply_capitalize(text: str):
        # This simulates calling our internal logic via the decorator wrapper on top of a function that returns text
        processed = process_text(text)
        return capitalize_words(processed)

    sample_inputs = [
        "hello world",
        "python programming is fun!",
        "   multiple spaces here   ",
        "no words at all 123"
    ]

    print("Sample Inputs and Outputs:")
    for input_str in sample_inputs:
        output_str = apply_capitalize(input_str)
        print(f'Input: "{input_str}"')
        print(f'Output: "{output_str}"\n')