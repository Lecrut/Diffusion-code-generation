def capitalize_first_letter(s):
    def capitalize_word(word):
        if not word:
            return word
        return word[0].upper() + word[1:].lower()
    
    return ' '.join(capitalize_word(word) for word in s.split())

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = capitalize_first_letter(sample_string)
    print(result)