def is_valid_string(phrase):
    return isinstance(phrase, str)

def calculate_phrase_length(phrase):
    if not is_valid_string(phrase):
        raise ValueError("Input must be a string")
    return len(phrase)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    try:
        print(calculate_phrase_length(sample_input))
    except ValueError as e:
        print(e)