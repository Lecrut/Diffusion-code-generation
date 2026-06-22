def capitalize_first_letter_only(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    try:
        result = capitalize_first_letter_only(sample_input)
        print(result)
    except ValueError as e:
        print(e)