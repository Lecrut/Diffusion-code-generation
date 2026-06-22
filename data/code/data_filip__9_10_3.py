def remove_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   Hello World   "
    result = remove_whitespace(sample_string)
    print(result)