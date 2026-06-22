FIRST_WORD_INDEX = 0

def read_first_word_from_line(line):
    words = line.split()
    if words:
        return words[FIRST_WORD_INDEX]
    else:
        return ""

if __name__ == '__main__':
    sample_lines = [
        "Hello world",
        "Python programming is fun",
        "Read the documentation"
    ]
    for line in sample_lines:
        print(read_first_word_from_line(line))