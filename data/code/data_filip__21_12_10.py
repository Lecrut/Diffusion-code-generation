import struct
import array

def run_length_encode(byte_data: bytes) -> bytes:
    if not byte_data:
        return b''
    result = bytearray()
    length = len(byte_data)
    current_byte = byte_data[0]
    count = 1
    i = 1
    while i < length:
        byte_val = byte_data[i]
        if byte_val == current_byte and count < 255:
            count += 1
            i += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = byte_val
            count = 1
            i += 1
    result.append(count)
    result.append(current_byte)
    return bytes(result)
if __name__ == '__main__':
    sample_input = b'aabcccccaaa'
    sample_bytes = sample_input.encode('ascii')
    encoded = run_length_encode(sample_bytes)
    print(encoded.hex())
    print(len(encoded))
    print(repr(encoded))