def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = capitalize_words(sample_input)
    print(result)