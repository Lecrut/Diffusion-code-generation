class NameParser:
    def parse(self, tab_separated_string):
        if not isinstance(tab_separated_string, str) or '\t' not in tab_separated_string:
            raise ValueError("Input must be a non-empty string containing at least one tab character.")
        return tab_separated_string.split('\t')

if __name__ == '__main__':
    parser = NameParser()
    sample_input = "Alice\tBob\tCharlie"
    result = parser.parse(sample_input)
    print(result)