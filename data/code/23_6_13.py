import sys

def rle_encode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    i = 0
    n = len(data)
    
    while i < n:
        current_byte = data[i]
        count = 1
        i += 1
        
        while i < n and data[i] == current_byte and count < 255:
            count += 1
            i += 1
        
        result.append(count)
        result.append(current_byte)
    
    return result

def rle_decode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    i = 0
    n = len(data)
    
    while i < n:
        count = data[i]
        value = data[i + 1]
        result.extend([value] * count)
        i += 2
    
    return result

if __name__ == '__main__':
    sample_input = bytearray([0, 0, 0, 5, 5, 5, 5, 5, 1, 1, 255, 255, 255, 255, 255, 255, 255, 255, 255, 3])
    encoded = rle_encode(sample_input)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    original = bytearray([0, 0, 0, 5, 5, 5, 5, 5, 1, 1, 255, 255, 255, 255, 255, 255, 255, 255, 255, 3])
    print(decoded == original)
    
    large_data = bytearray([42] * 10000)
    large_encoded = rle_encode(large_data)
    print(len(large_encoded))
    large_decoded = rle_decode(large_encoded)
    print(len(large_decoded))
    print(large_decoded == large_data)