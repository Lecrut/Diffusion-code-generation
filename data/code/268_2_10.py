def first_word_in_multiline_string(multiline_str):
    lines = multiline_str.strip().split('\n')
    for line in lines:
        if line.strip():
            return line.split()[0]

if __name__ == '__main__':
    sample_text = """This is a sample text.
It contains multiple lines,
and we need to find the first word."""
    print(first_word_in_multiline_string(sample_text))