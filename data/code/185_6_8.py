import re
WHITESPACE_PATTERN = '\\s+$'

def line_generator(text):
    lines = text.splitlines()
    for line in lines:
        stripped_line = re.sub(WHITESPACE_PATTERN, '', line)
        if stripped_line:
            yield stripped_line
if __name__ == '__main__':
    sample_text = 'This is a multi-line\ntext with some lines being empty,\nand others having trailing spaces.\n'
    for line in line_generator(sample_text):
        print(line)