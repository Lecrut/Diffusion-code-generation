def to_upper_hex(n):
    if n < 0:
        raise ValueError("Only non-negative integers are supported")
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    result = ""
    while n > 0:
        remainder = n & 15
        digit = hex_chars[remainder]
        result = digit + result
        n >>= 4
    return result

def transform_list_to_hex(binary_list):
    result_list = []
    for num in binary_list:
        if not isinstance(num, int) or num < 0:
            raise ValueError(f"Invalid integer in list: {num}")
        hex_str = to_upper_hex(num)
        result_list.append(hex_str)
    return result_list

if __name__ == '__main__':
    sample_data = [0, 1, 15, 16, 255, 256, 4095, 65535, 123456789]
    converted_values = transform_list_to_hex(sample_data)
    print(converted_values)