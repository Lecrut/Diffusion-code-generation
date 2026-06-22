def first_word(text):
    lines = text.strip().split('\n')
    for line in lines:
        if line.strip():
            return line.split()[0]
    return ''

if __name__ == '__main__':
    sample_text = "   Hello, world!\n\nThis is a test.\n"
    print(first_word(sample_text))