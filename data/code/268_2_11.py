def first_word_in_multiline_string(multiline_str):
    lines = multiline_str.strip().split('\n')
    for line in lines:
        words = line.split()
        if words:
            return words[0]
    return None

if __name__ == '__main__':
    sample_text = """This is a multi-line
string. The first word is 'This'.
"""
    print(first_word_in_multiline_string(sample_text))