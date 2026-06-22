def first_word_multiline(s):
    lines = s.strip().split('\n')
    for line in lines:
        if line.strip():
            return line.split()[0]
    return ''

if __name__ == '__main__':
    sample_text = "   Hello, world!\n\nThis is a test.\n  Leading and trailing spaces. "
    print(first_word_multiline(sample_text))