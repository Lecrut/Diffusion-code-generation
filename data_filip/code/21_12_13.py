import sys

def encode_rle(data: bytes) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    count = 1
    total_len = len(data)
    current_byte = data[0]
    
    for i in range(1, total_len):
        next_byte = data[i]
        if next_byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = next_byte
            count = 1
    
    result.append(count)
    result.append(current_byte)
    
    return result

if __name__ == '__main__':
    sample_data = b'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    encoded_result = encode_rle(sample_data)
    print(encoded_result)