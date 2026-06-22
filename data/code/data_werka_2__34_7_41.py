def capitalize_first_letter_of_each_word(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

if __name__ == '__main__':
    sample_input = "hello world! this is a TEST string."
    result = capitalize_first_letter_of_each_word(sample_input)
    print(result)