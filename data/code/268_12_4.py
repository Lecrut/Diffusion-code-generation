def first_word(s):
    lines = s.strip().split('\n')
    for line in lines:
        if line.strip():
            return line.split()[0]
    return ''

if __name__ == '__main__':
    sample_string = "   Hello, world!\n\nThis is a test.\n"
    print(first_word(sample_string))