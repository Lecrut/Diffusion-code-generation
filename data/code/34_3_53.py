def capitalize_first_letter(s):
    def capitalize_word(word):
        return word[0].upper() + word[1:].lower()
    
    words = s.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "multiple WORDS with DIFFERENT cases"
    result = capitalize_first_letter(sample_string)
    print(result)