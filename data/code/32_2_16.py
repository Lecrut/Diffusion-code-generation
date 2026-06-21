def binary_to_hex(binary_input: bytes) -> str:
    if not isinstance(binary_input, bytes):
        raise TypeError('Input must be bytes')
    return binary_input.hex()

def process_data(binary_input: bytes) -> dict:
    hex_str = binary_to_hex(binary_input)
    return {'hex': hex_str, 'length': len(binary_input), 'hex_length': len(hex_str)}

def validate_and_convert(binary_input: bytes) -> str:
    if len(binary_input) == 0:
        raise ValueError('Input cannot be empty')
    return binary_to_hex(binary_input)
if __name__ == '__main__':
    sample_binary = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
    result = process_data(sample_binary)
    print(result)
    hex_str = validate_and_convert(sample_binary)
    print(hex_str)
    print(binary_to_hex(b''))