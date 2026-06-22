import struct

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    result = bytearray()
    i = 0
    n = len(data)
    while i < n:
        current_byte = data[i]
        count = 1
        while i + count < n and data[i + count] == current_byte and count < 255:
            count += 1
        result.append(current_byte)
        result.append(count)
        i += count
    return bytes(result)

def run_length_decode(data: bytes) -> bytes:
    if not data:
        return b''
    result = bytearray()
    i = 0
    n = len(data)
    while i < n:
        byte_val = data[i]
        count = data[i + 1]
        result.extend(bytes([byte_val] * count))
        i += 2
    return bytes(result)

if __name__ == '__main__':
    sample_data = bytes([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5])
    encoded = run_length_encode(sample_data)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)