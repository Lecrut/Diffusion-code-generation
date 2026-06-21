def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    try:
        capitalized_string = capitalize_first_letter(sample_string)
        print(capitalized_string)
    except ValueError as e:
        print(e)