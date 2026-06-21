def capitalize_first_letter_only(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def capitalize(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = s.split()
    capitalized_words = map(capitalize, words)
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    try:
        result = capitalize_first_letter_only(sample_input)
        print(result)
    except ValueError as e:
        print(e)