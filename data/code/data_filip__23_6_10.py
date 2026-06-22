import sys
from typing import List, Tuple, Union

def run_length_encode(data: Union[bytes, bytearray]) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    count = 1
    length = len(data)
    current_byte = data[0]
    
    for i in range(1, length):
        next_byte = data[i]
        if next_byte == current_byte and count < 255:
            count += 1
        else:
            result.append(current_byte)
            result.append(count)
            current_byte = next_byte
            count = 1
    
    result.append(current_byte)
    result.append(count)
    
    return result

def run_length_decode(encoded: Union[bytes, bytearray]) -> bytearray:
    if not encoded:
        return bytearray()
    
    result = bytearray()
    length = len(encoded)
    
    i = 0
    while i < length:
        value = encoded[i]
        count = encoded[i + 1]
        result.extend([value] * count)
        i += 2
    
    return result

if __name__ == '__main__':
    sample_data = bytes([255, 255, 255, 255, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 255])
    
    encoded = run_length_encode(sample_data)
    decoded = run_length_decode(encoded)
    
    print(f"Original: {list(sample_data)}")
    print(f"Encoded:  {list(encoded)}")
    print(f"Decoded:  {list(decoded)}")
    print(f"Match:    {sample_data == bytes(decoded)}")