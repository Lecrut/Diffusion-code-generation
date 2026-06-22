def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "hello world this is a test"
    try:
        CAPITALIZED_STRING = capitalize_first_letter(SAMPLE_STRING)
        print(CAPITALIZED_STRING)
    except ValueError as e:
        print(e)