def line_generator(text):
    for line in text.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a multi-line
text with   extra spaces and
empty lines.

Here are some lines.
"""
    for line in line_generator(sample_text):
        print(line)