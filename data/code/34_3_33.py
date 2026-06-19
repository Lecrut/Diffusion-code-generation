def capitalize_words(input_text):
    return ' '.join(word.capitalize() for word in input_text.split())

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    result = capitalize_words(sample_input)
    print(result)