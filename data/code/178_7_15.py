def split_multiple_whitespaces(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "  This   is a\ttest\nstring  "
    tokens = split_multiple_whitespaces(sample_text)
    print(tokens)