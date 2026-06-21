class NameParser:
    DELIMITER = ';'

    @staticmethod
    def parse_names(line):
        return [name.strip() for name in line.split(NameParser.DELIMITER) if name]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    parsed_names = NameParser.parse_names(sample_line)
    print(parsed_names)