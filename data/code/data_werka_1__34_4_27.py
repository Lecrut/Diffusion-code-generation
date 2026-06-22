def capitalize_first_letter(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    result = capitalize_first_letter(sample_input)
    print(result)