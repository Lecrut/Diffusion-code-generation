def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   Hello, World!   "
    result = trim_spaces(sample_string)
    print(result)