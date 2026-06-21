class NameParser:
    DELIMITER = '\t'
    
    @staticmethod
    def parse_names(tab_separated_string):
        return tab_separated_string.split(NameParser.DELIMITER)

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie"
    result = NameParser.parse_names(sample_input)
    print(result)