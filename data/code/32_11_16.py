import re
import binascii

def binary_strings_to_hex(binary_strings):
    hex_results = []
    for binary_str in binary_strings:
        if not isinstance(binary_str, str):
            raise ValueError(f'Expected string, got {type(binary_str).__name__}')
        if not re.match('^[01]*$', binary_str):
            raise ValueError(f"Invalid binary string: '{binary_str}'. Contains non-binary characters.")
        if len(binary_str) % 8 != 0:
            raise ValueError(f"Binary string length must be a multiple of 8: '{binary_str}' has length {len(binary_str)}")
        if not binary_str:
            raise ValueError('Empty binary string is not allowed')
        int_value = int(binary_str, 2)
        hex_str = format(int_value, 'x').upper()
        hex_results.append(hex_str)
    return hex_results
if __name__ == '__main__':
    sample_binary_strings = ['00001111', '11110000', '10101010', '11001100', '00000001', '00000010', '00000100', '00001000']
    result = binary_strings_to_hex(sample_binary_strings)
    print(result)