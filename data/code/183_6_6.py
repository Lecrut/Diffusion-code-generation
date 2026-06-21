def parse_names(tab_separated_string):
    return tab_separated_string.split('\t')

if __name__ == '__main__':
    sample_input = "Eve\tFrank\tGrace"
    result = parse_names(sample_input)
    print(result)