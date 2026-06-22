def trim_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   \t  \n  this is a test string with excessive whitespace  \n  \t  "
    result = trim_whitespace(sample_string)
    print(result)