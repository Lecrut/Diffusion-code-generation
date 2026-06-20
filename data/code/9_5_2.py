def trim_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   \t  This is a sample string with excessive whitespace.   \n  "
    result = trim_whitespace(sample_string)
    print(result)