def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    words = s.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    try:
        capitalized_string = capitalize_first_letter(sample_string)
        print(capitalized_string)
    except ValueError as e:
        print(e)