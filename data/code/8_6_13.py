def parse_strings(input_string):
    if not input_string:
        return []
    return [s.strip() for s in input_string.split(',') if s.strip()]

if __name__ == '__main__':
    sample_data = "  apple  , banana , ,  orange  ,  , grape "
    result = parse_strings(sample_data)
    print(result)