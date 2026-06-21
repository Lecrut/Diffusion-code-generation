def line_generator(text):
    for line in text.splitlines():
        if line.strip():
            yield line.strip()

if __name__ == '__main__':
    sample_text = """This is a multi-line
text with some lines being empty,
and others having trailing spaces.   
"""
    for line in line_generator(sample_text):
        print(line)