def first_word_in_line(line):
    return line.split()[0]

if __name__ == '__main__':
    sample_lines = [
        "Hello world",
        "Python programming is fun",
        "Read the documentation"
    ]
    for line in sample_lines:
        print(first_word_in_line(line))