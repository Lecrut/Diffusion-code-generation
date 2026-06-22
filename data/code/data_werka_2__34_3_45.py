def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def capitalize_word(word):
        if len(word) > 0:
            return word[0].upper() + word[1:].lower()
        return word
    
    words = s.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = capitalize_first_letter(sample_string)
    print(result)