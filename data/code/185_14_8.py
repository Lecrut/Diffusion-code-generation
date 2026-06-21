def parse_key_value_pairs(input_string):
    result = {}
    for pair in input_string.split():
        key, value = pair.split('=')
        result[key.strip()] = value.strip()
    return result

if __name__ == '__main__':
    sample_input = "key1=value1 key2  =value2 key3=value3"
    print(parse_key_value_pairs(sample_input))