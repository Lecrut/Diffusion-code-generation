def capitalize_first_letter_only(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def is_valid_word(word):
        return word.isalpha() or any(char.isdigit() for char in word)
    
    words = s.split()
    capitalized_words = []
    
    for word in words:
        if is_valid_word(word):
            capitalized_words.append(word[0].upper() + word[1:] if word else '')
        else:
            capitalized_words.append(word)
    
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test 123"
    try:
        result = capitalize_first_letter_only(sample_input)
        print(result)
    except ValueError as e:
        print(e)