MAX_WORD_LENGTH = 100

def extract_first_word(input_string):
    if not isinstance(input_string, str) or len(input_string) > MAX_WORD_LENGTH:
        raise ValueError("Input must be a non-empty string with max length of 100")
    
    words = input_string.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_input = "This is a sample string to test the function"
    try:
        result = extract_first_word(sample_input)
        print(result)
    except ValueError as e:
        print(e)