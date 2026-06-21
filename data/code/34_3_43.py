def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s.strip():
        raise ValueError("Input string cannot be empty or only whitespace")

def capitalize_first_letter(s):
    validate_input(s)
    words = s.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "this is a test string with multiple words"
    result = capitalize_first_letter(sample_string)
    print(result)