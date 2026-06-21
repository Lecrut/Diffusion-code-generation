def split_multiple_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello   World\tThis\nis a test"
    print(split_multiple_whitespace(sample_text))