def get_first_word(multi_line_string):
    lines = multi_line_string.split('\n')
    for line in lines:
        words = line.split()
        if words:
            return words[0]

if __name__ == '__main__':
    sample_text = """This is a sample text.
It contains multiple lines.
The first word is 'This'."""
    print(get_first_word(sample_text))