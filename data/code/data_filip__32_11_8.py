def binary_to_hex(binary_string):
    for char in binary_string:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid binary character '{char}' in input '{binary_string}'")
    if not binary_string:
        raise ValueError("Empty string provided")
    decimal_value = int(binary_string, 2)
    return format(decimal_value, 'X')

def process_binary_list(binary_list):
    results = []
    for binary_str in binary_list:
        hex_value = binary_to_hex(binary_str)
        results.append(hex_value)
    return results

if __name__ == '__main__':
    sample_data = [
        "1010",
        "11110000",
        "100100110101",
        "0000",
        "1111111111111111"
    ]
    converted_values = process_binary_list(sample_data)
    print(converted_values)