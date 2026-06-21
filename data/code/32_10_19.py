def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return '0'
    decimal_value = int(binary_str, 2)
    if decimal_value == 0:
        return '0'
    is_negative = False
    if binary_str.startswith('-'):
        is_negative = True
        binary_str = binary_str[1:]
    if len(binary_str) == 0:
        return '0'
    decimal_value = int(binary_str, 2)
    if is_negative:
        hex_str = hex(decimal_value)[2:]
        return hex_str
    hex_str = hex(decimal_value)[2:]
    return hex_str
if __name__ == '__main__':
    print(binary_to_hex('11111111'))
    print(binary_to_hex('00001010'))
    print(binary_to_hex('0'))
    print(binary_to_hex('101010101010'))