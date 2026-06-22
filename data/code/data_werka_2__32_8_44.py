def calculate_phrase_length(phrase):
    def validate_input(input_data):
        if not isinstance(input_data, str):
            raise ValueError("Input must be a string")
    
    validate_input(phrase)
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