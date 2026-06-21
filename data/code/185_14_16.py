def parse_kv_pairs(kv_string):
    result = {}
    for pair in kv_string.split():
        key, value = pair.split('=', 1)
        result[key.strip()] = value.strip()
    return result

if __name__ == '__main__':
    sample_input = "key1=value1 key2= value2 key3=value3"
    parsed_dict = parse_kv_pairs(sample_input)
    print(parsed_dict)