class FirstWordExtractor:
    @staticmethod
    def get_first_word(line):
        return line.split()[0]

if __name__ == '__main__':
    sample_lines = [
        "Hello world",
        "Python programming is fun",
        "Read the documentation"
    ]
    extractor = FirstWordExtractor()
    for line in sample_lines:
        print(extractor.get_first_word(line))