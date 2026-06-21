def parse_names(tab_separated_string):
    if not isinstance(tab_separated_string, str) or '\t' not in tab_separated_string:
        raise ValueError("Input must be a non-empty string containing at least one tab character.")
    return tab_separated_string.split('\t')

if __name__ == '__main__':
    sample_input = "John\tDoe\tJane"
    result = parse_names(sample_input)
    print(result)