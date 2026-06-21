def capitalize_first_letter_of_each_word(input_string):
    def capitalize_word(word):
        if not word:
            return ''
        return word[0].upper() + word[1:]
    
    words = input_string.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world! this is a TEST string."
    result = capitalize_first_letter_of_each_word(sample_input)
    print(result)