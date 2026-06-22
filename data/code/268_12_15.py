def first_word_in_multiline_string(multiline_str):
    lines = multiline_str.strip().split('\n')
    for line in lines:
        word = line.split()[0]
        if word:
            return word

if __name__ == '__main__':
    sample_text = "   Hello, world!\n\nThis is a test.\n"
    print(first_word_in_multiline_string(sample_text))