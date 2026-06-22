def get_phrase_length(input_string):
    return len(input_string.strip())

if __name__ == '__main__':
    sample_values = ["", "   ", "Hello, World!", "  Python Programming  ", "\t\nWhitespace\t\n"]
    for value in sample_values:
        print(get_phrase_length(value))