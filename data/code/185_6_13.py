def strip_and_filter_lines(text):
    for line in text.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a multi-line
text with some lines being empty,
and others having trailing spaces.
"""
    for line in strip_and_filter_lines(sample_text):
        print(line)