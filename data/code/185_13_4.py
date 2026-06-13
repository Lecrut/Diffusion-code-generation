import re
def parse_key_value_string(data_string):
    result = {}
    pairs = data_string.split()
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key] = value
    return result
if __name__ == '__main__':
    test_string_1 = "name: Alice age: 30 city: New York"
    parsed_dict_1 = parse_key_value_string(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: {parsed_dict_1}")
    test_string_2 = "product: apple, price: 1.00, in_stock: true"
    parsed_dict_2 = parse_key_value_string(test_string_2)
    print(f"Input: '{test_string_2}'")
    print(f"Output: {parsed_dict_2}")
    test_string_3 = "only_one: value1 another: value2"
    parsed_dict_3 = parse_key_value_string(test_string_3)
    print(f"Input: '{test_string_3}'")
    print(f"Output: {parsed_dict_3}")