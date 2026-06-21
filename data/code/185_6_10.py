def line_generator(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    for line in text.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a multi-line
text with some lines being empty,
and others having trailing spaces.
"""
    try:
        for line in line_generator(sample_text):
            print(line)
    except ValueError as e:
        print(e)