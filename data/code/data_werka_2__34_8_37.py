def capitalize_first_letter_only(s):
    def capitalize(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = s.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    SAMPLE_INPUT = "hello world this is a test"
    result = capitalize_first_letter_only(SAMPLE_INPUT)
    print(result)