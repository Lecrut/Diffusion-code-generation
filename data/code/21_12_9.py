import struct
import array

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    run_length = 0
    current_byte = data[0]
    
    length = len(data)
    for i in range(length):
        byte_val = data[i]
        if byte_val == current_byte:
            run_length += 1
        else:
            while run_length > 0:
                count = run_length
                if count > 255:
                    chunk = 255
                    count = 255
                    run_length -= 255
                    result.append(count)
                    result.append(current_byte)
                else:
                    result.append(count)
                    result.append(current_byte)
                    run_length = 0
            current_byte = byte_val
            run_length = 1
            
    while run_length > 0:
        count = run_length
        if count > 255:
            chunk = 255
            count = 255
            run_length -= 255
            result.append(count)
            result.append(current_byte)
        else:
            result.append(count)
            result.append(current_byte)
            run_length = 0
            
    return bytes(result)

if __name__ == '__main__':
    sample_data = b"AAABBBCCCD"
    encoded = run_length_encode(sample_data)
    print(encoded)