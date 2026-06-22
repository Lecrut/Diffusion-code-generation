def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    capitalized_output = capitalize_first_letter(sample_input)
    print(capitalized_output)