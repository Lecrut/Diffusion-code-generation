def binary_to_hex(binary_input):
    if isinstance(binary_input, str):
        return hex(int(binary_input, 2))[2:].upper()
    elif isinstance(binary_input, (bytes, bytearray)):
        return binary_input.hex().upper()
    else:
        raise TypeError('Input must be a string (binary) or bytes object')
if __name__ == '__main__':
    sample_bin_str = '10101011'
    sample_bin_bytes = b'\xab'
    print(binary_to_hex(sample_bin_str))
    print(binary_to_hex(sample_bin_bytes))