def parse_string(data_string):
    result = {}
    pairs = data_string.split()
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key] = value
    return result
if __name__ == '__main__':
    sample_input = "name: Alice age: 30 city: New York"
    parsed_data = parse_string(sample_input)
    print(parsed_data)