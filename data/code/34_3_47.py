def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s.strip():
        raise ValueError("Input string cannot be empty or whitespace only")

def capitalize_first_letter(s):
    validate_input(s)
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "this is another test string"
    try:
        result = capitalize_first_letter(sample_string)
        print(result)
    except ValueError as e:
        print(e)