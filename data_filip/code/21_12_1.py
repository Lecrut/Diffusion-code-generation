import struct

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    length = len(data)
    i = 0
    
    while i < length:
        current_byte = data[i]
        run_length = 1
        while i + run_length < length and data[i + run_length] == current_byte:
            run_length += 1
        
        if run_length > 1:
            result.append(current_byte)
            result.append(run_length)
        else:
            result.append(current_byte)
        
        i += run_length
    
    return bytes(result)

if __name__ == '__main__':
    sample_data = b"AABBBBBCCD"
    encoded_data = run_length_encode(sample_data)
    print(encoded_data)