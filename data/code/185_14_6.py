def parse_kv_pairs(kv_string):
    kv_dict = {}
    for pair in kv_string.split():
        key, value = pair.strip().split('=')
        kv_dict[key] = value
    return kv_dict

if __name__ == '__main__':
    sample_input = "key1=value1 key2=value2 key1=new_value1"
    result = parse_kv_pairs(sample_input)
    print(result)