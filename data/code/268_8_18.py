def first_word_from_line(line):
    return line.split()[0]

if __name__ == '__main__':
    sample_lines = [
        "Hello world",
        "Python programming is fun",
        "Read this file"
    ]
    for line in sample_lines:
        print(first_word_from_line(line))