def first_word(s):
    lines = s.strip().split('\n')
    for line in lines:
        words = line.split()
        if words:
            return words[0]
    return ''

if __name__ == '__main__':
    sample_string = "   Hello, world!\n\nThis is a test.\n"
    print(first_word(sample_string))