def first_word(s):
    lines = s.strip().split('\n')
    for line in lines:
        word = line.split()[0]
        if word:
            return word

if __name__ == '__main__':
    sample_string = "   Hello, world!\n   This is a test.\n"
    print(first_word(sample_string))