def line_generator(text):
    for line in text.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a sample text.
It has multiple lines,
and some trailing spaces   .
There are also empty lines above and below.

End of sample."""
    
    for line in line_generator(sample_text):
        print(line)