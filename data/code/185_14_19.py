KEY_VALUE_DELIMITER = '='
WHITESPACE_CHARS = ' \t\n\r'

def parse_kv_pairs(kv_string):
    result = {}
    pairs = kv_string.split()
    for pair in pairs:
        key, value = pair.split(KEY_VALUE_DELIMITER, 1)
        result[key.strip(WHITESPACE_CHARS)] = value.strip(WHITESPACE_CHARS)
    return result

if __name__ == '__main__':
    sample_input = "key1=value1 key2= value2 key1= value3"
    print(parse_kv_pairs(sample_input))