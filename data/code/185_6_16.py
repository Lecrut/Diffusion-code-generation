def memory_efficient_lines(text):
    for line in text.splitlines():
        stripped_line = line.rstrip()
        if stripped_line:
            yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a multi-line string.
It contains various lines, some of which are empty or have trailing spaces.

Here's another line with trailing spaces.   """
    for line in memory_efficient_lines(sample_text):
        print(line)