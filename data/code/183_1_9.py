class NameParser:
    DELIMITER = ';'

    @staticmethod
    def parse_names(line):
        if not isinstance(line, str) or NameParser.DELIMITER not in line:
            raise ValueError("Invalid input: expected a semicolon-delimited string")
        names = [name.strip() for name in line.split(NameParser.DELIMITER) if name]
        return names

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    try:
        parser = NameParser()
        print(parser.parse_names(sample_line))
    except ValueError as e:
        print(e)