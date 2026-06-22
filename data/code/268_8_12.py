def extract_first_word(line):
    return line.split()[0]

if __name__ == '__main__':
    sample_lines = [
        "This is the first line of the file.",
        "Python programming is fun",
        "Read the documentation"
    ]
    for line in sample_lines:
        print(extract_first_word(line))