def capitalize_words(input_string):
    return input_string.title()

if __name__ == '__main__':
    sample_string = "hello world from alibaba cloud"
    capitalized_string = capitalize_words(sample_string)
    print(capitalized_string)