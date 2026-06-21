def capitalize_first_letter_only(s):
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = s.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = capitalize_first_letter_only(sample_input)
    print(result)