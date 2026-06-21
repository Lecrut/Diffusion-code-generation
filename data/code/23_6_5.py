import sys

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    result = bytearray()
    current_byte = data[0]
    count = 1
    max_count = 255
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < max_count:
            count += 1
        else:
            result.append(current_byte)
            result.append(count)
            current_byte = byte
            count = 1
    result.append(current_byte)
    result.append(count)
    return bytes(result)

def run_length_decode(encoded_data: bytes) -> bytes:
    if not encoded_data:
        return b""
    if len(encoded_data) % 2 != 0:
        raise ValueError("Invalid RLE data: odd length")
    result = bytearray()
    for i in range(0, len(encoded_data), 2):
        byte = encoded_data[i]
        count = encoded_data[i + 1]
        result.extend([byte] * count)
    return bytes(result)

if __name__ == '__main__':
    sample_input = b"A" * 10 + b"B" * 5 + b"C" * 200 + b"D"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    is_match = sample_input == decoded
    print(is_match)