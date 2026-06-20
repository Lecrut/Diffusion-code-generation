def trim_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   \n\t  excessive whitespace   \n  "
    print(trim_whitespace(sample_string))