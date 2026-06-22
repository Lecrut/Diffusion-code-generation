def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    def validate_input(input_str):
        if not isinstance(input_str, str):
            return False
        return True
    
    if not validate_input(phrase):
        raise ValueError("Input validation failed")
    
    return len(phrase)

if __name__ == '__main__':
    sample_phrases = [
        "Hello, World!",
        "Optimized function",
        "",
        "Python programming"
    ]
    
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))