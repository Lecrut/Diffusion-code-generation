import sys

RUN_LENGTH_LIMIT = 255
EMPTY_BYTES_RESULT = bytearray()

def encode_rle_optimized(data: bytes) -> bytearray:
    if not data:
        return EMPTY_BYTES_RESULT
    
    result = bytearray()
    n = len(data)
    i = 0
    
    while i < n:
        current_val = data[i]
        count = 1
        
        while i + count < n and count < RUN_LENGTH_LIMIT and data[i + count] == current_val:
            count += 1
        
        result.append(count)
        result.append(current_val)
        i += count
    
    return result

def decode_rle_optimized(encoded: bytearray) -> bytearray:
    if not encoded:
        return EMPTY_BYTES_RESULT
    
    result = bytearray()
    i = 0
    length = len(encoded)
    
    while i < length:
        count = encoded[i]
        value = encoded[i + 1]
        result.extend([value] * count)
        i += 2
    
    return result

if __name__ == '__main__':
    sample_input = b'AAABBBBCCCCDDDEEEEEFFFFFFFFFGG'
    encoded_result = encode_rle_optimized(sample_input)
    decoded_result = decode_rle_optimized(encoded_result)
    
    print(f"Original: {sample_input}")
    print(f"Encoded bytes: {list(encoded_result)}")
    print(f"Decoded: {bytes(decoded_result)}")
    print(f"Round-trip match: {sample_input == bytes(decoded_result)}")