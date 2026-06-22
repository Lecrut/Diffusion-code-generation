def first_word_in_multiline_string(multiline_string):
    lines = multiline_string.split('\n')
    for line in lines:
        words = line.split()
        if words:
            return words[0]
    return None

if __name__ == '__main__':
    sample_text = """Hello world,
this is a test.
Python programming."""
    print(first_word_in_multiline_string(sample_text))