def parse_names(tab_separated_string):
    return tab_separated_string.split('\t')

if __name__ == '__main__':
    SAMPLE_INPUT = "Alice\tBob\tCharlie"
    result = parse_names(SAMPLE_INPUT)
    print(result)