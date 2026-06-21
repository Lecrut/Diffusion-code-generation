class NameParser:
    SEPARATOR = ';'

    @staticmethod
    def parse(line):
        return [name.strip() for name in line.split(NameParser.SEPARATOR) if name]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    print(NameParser.parse(sample_line))