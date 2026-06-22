def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = trim_spaces(sample_input)
    print(result)