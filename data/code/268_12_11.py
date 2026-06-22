def first_word_multiline(s):
    lines = s.strip().split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            return stripped_line.split()[0]
    return ''

if __name__ == '__main__':
    sample_text = "   Hello, world!\n\nThis is a test.\n  Leading and trailing spaces. "
    print(first_word_multiline(sample_text))