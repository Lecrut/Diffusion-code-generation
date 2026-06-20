def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample = "  hello world  "
    result = strip_whitespace(sample)
    print(result)