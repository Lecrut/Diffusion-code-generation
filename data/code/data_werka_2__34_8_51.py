def capitalize_first_letter_only(s):
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = s.split()
    capitalized_words = [capitalize_word(word) for word in words]
    result = ' '.join(capitalized_words)
    return result

if __name__ == '__main__':
    sample_input = "this is an example sentence"
    try:
        result = capitalize_first_letter_only(sample_input)
        print(result)
    except ValueError as e:
        print(e)