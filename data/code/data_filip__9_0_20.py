def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_text = "   Hello World   "
    result = strip_whitespace(sample_text)
    print(result)