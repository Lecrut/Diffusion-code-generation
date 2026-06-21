def parse_names(tab_separated_string):
    return tab_separated_string.split('\t')

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie"
    print(parse_names(sample_input))