def lines_generator(text):
    for line in text.splitlines():
        stripped_line = line.rstrip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a sample text.
It has multiple lines,
and some trailing spaces.  
"""

    for line in lines_generator(sample_text):
        print(line)