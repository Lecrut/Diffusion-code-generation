SEPARATOR = '\t'

def parse_names(tab_separated_string):
    return tab_separated_string.split(SEPARATOR)

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie"
    result = parse_names(sample_input)
    print(result)