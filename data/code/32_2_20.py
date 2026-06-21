def binary_to_hex(data: bytes) -> str:
    if not isinstance(data, bytes):
        data = bytes(data)
    hex_str = data.hex()
    if len(hex_str) == 0:
        return "0x0"
    result = "0x" + hex_str
    return result

if __name__ == '__main__':
    sample_data = bytes([255, 0, 16, 10, 255])
    result = binary_to_hex(sample_data)
    print(result)