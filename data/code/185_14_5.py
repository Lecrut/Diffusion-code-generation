def parse_key_value_pairs(pair_string):
    result = {}
    for pair in pair_string.split():
        key, value = pair.split('=')
        result[key.strip()] = value.strip()
    return result

if __name__ == '__main__':
    sample_input = "key1=value1 key2=value2 key1=newvalue"
    print(parse_key_value_pairs(sample_input))