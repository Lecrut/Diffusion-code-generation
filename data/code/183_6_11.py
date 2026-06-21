class NameParser:
    DELIMITER = '\t'

    @staticmethod
    def parse_names(tab_separated_string):
        if not isinstance(tab_separated_string, str) or NameParser.DELIMITER not in tab_separated_string:
            raise ValueError("Input must be a non-empty string containing at least one tab character.")
        return tab_separated_string.split(NameParser.DELIMITER)

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie"
    result = NameParser.parse_names(sample_input)
    print(result)