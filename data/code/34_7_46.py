def capitalize_first_letter_of_each_word(input_string):
    def is_valid_input(s):
        return isinstance(s, str)
    
    if not is_valid_input(input_string):
        raise ValueError("Input must be a string")
    
    words = input_string.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "yet another example with different casing."
    result = capitalize_first_letter_of_each_word(sample_input)
    print(result)