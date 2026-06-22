import struct

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    
    result = bytearray()
    n = len(data)
    i = 0
    
    while i < n:
        current_byte = data[i]
        count = 1
        while i + count < n and data[i + count] == current_byte and count < 255:
            count += 1
        
        result.append(count)
        result.append(current_byte)
        i += count
    
    return bytes(result)

if __name__ == '__main__':
    sample1 = b'AAABBCCD'
    print(run_length_encode(sample1))
    
    sample2 = b''
    print(run_length_encode(sample2))
    
    sample3 = b'AB'
    print(run_length_encode(sample3))
    
    sample4 = b'A' * 300
    print(run_length_encode(sample4))
    
    sample5 = bytes(range(256))
    print(run_length_encode(sample5))