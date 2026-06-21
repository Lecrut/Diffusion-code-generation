import ctypes
import array

def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    
    encoded = bytearray()
    length = len(data)
    i = 0
    
    while i < length:
        current_byte = data[i]
        count = 1
        
        while i + count < length and data[i + count] == current_byte and count < 255:
            count += 1
        
        encoded.append(current_byte)
        encoded.append(count)
        i += count
    
    return bytes(encoded)

if __name__ == '__main__':
    sample1 = b'AAABBBCCD'
    result1 = run_length_encode(sample1)
    print(result1)
    
    sample2 = b'ABC'
    result2 = run_length_encode(sample2)
    print(result2)
    
    sample3 = b'\x00\x00\x00\xFF\xFF'
    result3 = run_length_encode(sample3)
    print(result3)
    
    sample4 = b''
    result4 = run_length_encode(sample4)
    print(result4)