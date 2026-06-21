class NameParser:
    DELIMITER = ';'

    @staticmethod
    def parse(line):
        return [name.strip() for name in line.split(NameParser.DELIMITER) if name]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    parser = NameParser()
    print(parser.parse(sample_line))