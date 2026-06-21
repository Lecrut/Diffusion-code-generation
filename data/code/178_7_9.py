def split_multiple_whitespaces(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello   world\tthis\nis a test"
    print(split_multiple_whitespaces(sample_text))