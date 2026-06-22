def capitalize_first_letter_only(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = s.split()
    capitalized_words = (capitalize_word(word) for word in words)
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    SAMPLE_INPUT = "hello world this is a test"
    try:
        result = capitalize_first_letter_only(SAMPLE_INPUT)
        print(result)
    except ValueError as e:
        print(e)