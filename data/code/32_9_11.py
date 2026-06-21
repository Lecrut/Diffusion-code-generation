from binascii import unhexlify

def binary_to_hexadecimal(binary_string: str) -> str:
    cleaned = binary_string.replace(' ', '')
    if not cleaned:
        raise ValueError("Input cannot be empty")
    if not all(c in '01' for c in cleaned):
        raise ValueError("Input must contain only 0 and 1")
    if len(cleaned) % 8 != 0:
        padded = cleaned.zfill((len(cleaned) + 7) // 8 * 8)
    else:
        padded = cleaned
    byte_list = [padded[i:i+8] for i in range(0, len(padded), 8)]
    bytes_val = bytes([int(b, 2) for b in byte_list])
    return bytes_val.hex()

if __name__ == '__main__':
    result = binary_to_hexadecimal("01011010")
    print(result)