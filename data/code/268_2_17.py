def first_word_in_multiline_string(multi_line_str):
    lines = multi_line_str.split('\n')
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