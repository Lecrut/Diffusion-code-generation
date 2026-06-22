def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    capitalized_output = capitalize_words(sample_input)
    print(capitalized_output)