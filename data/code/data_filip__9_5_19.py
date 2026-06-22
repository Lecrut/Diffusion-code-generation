def trim_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   excessive whitespace   "
    result = trim_whitespace(sample_string)
    print(result)