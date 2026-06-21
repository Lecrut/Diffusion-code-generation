class NameParser:
    DELIMITER = '\t'
    
    @staticmethod
    def parse_names(tab_separated_string):
        if not isinstance(tab_separated_string, str) or not tab_separated_string.strip():
            raise ValueError("Input must be a non-empty string.")
        return tab_separated_string.split(NameParser.DELIMITER)

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie"
    parser = NameParser()
    result = parser.parse_names(sample_input)
    print(result)