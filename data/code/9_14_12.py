def clean_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = clean_whitespace(sample_input)
    print(result)