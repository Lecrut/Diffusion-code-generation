import re
def parse_key_value_string(data_string):
    result = {}
    pairs = data_string.split()
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key.strip()] = value.strip()
    return result
if __name__ == '__main__':
    sample_string = "name: Alice age: 30 city: New York"
    parsed_data = parse_key_value_string(sample_string)
    print(parsed_data)