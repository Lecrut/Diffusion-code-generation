class LineProcessor:
    def __init__(self, text):
        self.text = text

    def process_lines(self):
        for line in self.text.splitlines():
            stripped_line = line.strip()
            if stripped_line:
                yield stripped_line

if __name__ == '__main__':
    sample_text = """This is a multi-line
text with some lines being empty,
and others having trailing spaces.
"""
    processor = LineProcessor(sample_text)
    for line in processor.process_lines():
        print(line)