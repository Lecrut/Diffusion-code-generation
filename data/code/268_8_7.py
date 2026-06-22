def first_word_from_line(line):
    return line.split()[0]

if __name__ == '__main__':
    sample_lines = [
        "Hello world",
        "Python is great",
        "This is a test"
    ]
    for line in sample_lines:
        print(first_word_from_line(line))