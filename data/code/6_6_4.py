def convert_spaces_to_underscores(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_input = "Hello world example"
    result = convert_spaces_to_underscores(sample_input)
    print(result)