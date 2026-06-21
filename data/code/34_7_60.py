def capitalize_first_letter_of_each_word(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def capitalize(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = input_string.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world! this is a TEST string."
    try:
        result = capitalize_first_letter_of_each_word(sample_input)
        print(result)
    except ValueError as e:
        print(e)