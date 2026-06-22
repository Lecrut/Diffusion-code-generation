import struct

def rle_encode(data):
    if not data:
        return bytearray()
    
    encoded = bytearray()
    count = 1
    current = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            while count > 255:
                encoded.append(255)
                encoded.append(current)
                count -= 255
            encoded.append(count)
            encoded.append(current)
            current = data[i]
            count = 1
    
    while count > 255:
        encoded.append(255)
        encoded.append(current)
        count -= 255
    encoded.append(count)
    encoded.append(current)
    
    return encoded

def rle_decode(encoded):
    if not encoded:
        return bytearray()
    
    decoded = bytearray()
    i = 0
    while i < len(encoded):
        count = encoded[i]
        value = encoded[i + 1]
        decoded.extend([value] * count)
        i += 2
    
    return decoded

if __name__ == '__main__':
    sample_data = bytearray(b'AAAABBBCCDAA')
    encoded = rle_encode(sample_data)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)