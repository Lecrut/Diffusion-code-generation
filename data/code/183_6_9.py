class NameParser:
    def __init__(self, delimiter='\t'):
        self.delimiter = delimiter

    def parse(self, input_string):
        if not isinstance(input_string, str) or self.delimiter not in input_string:
            raise ValueError("Input must be a non-empty string containing at least one delimiter.")
        return input_string.split(self.delimiter)

if __name__ == '__main__':
    parser = NameParser()
    sample_input = "Alice\tBob\tCharlie"
    result = parser.parse(sample_input)
    print(result)