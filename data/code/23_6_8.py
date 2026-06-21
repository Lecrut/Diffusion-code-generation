import sys

def rle_encode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.extend([current_byte, count])
            current_byte = byte
            count = 1
    
    result.extend([current_byte, count])
    return result

def rle_decode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    if len(data) % 2 != 0:
        raise ValueError("Invalid RLE data length")
    
    for i in range(0, len(data), 2):
        value = data[i]
        count = data[i + 1]
        result.extend([value] * count)
    
    return result

if __name__ == '__main__':
    sample_data = bytearray([65] * 1000 + [66] * 500 + [67] * 1)
    encoded = rle_encode(sample_data)
    decoded = rle_decode(encoded)
    print(f"Original length: {len(sample_data)}")
    print(f"Encoded length: {len(encoded)}")
    print(f"Decoded matches original: {sample_data == decoded}")
    print(f"First 20 bytes of encoded: {list(encoded[:20])}")