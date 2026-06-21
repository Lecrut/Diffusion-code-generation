class NameParser:
    def parse(self, line):
        return [name.strip() for name in line.split(';') if name]

if __name__ == '__main__':
    parser = NameParser()
    sample_line = "Alice; Bob; Charlie; David"
    print(parser.parse(sample_line))