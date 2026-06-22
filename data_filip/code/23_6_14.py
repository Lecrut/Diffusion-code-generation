def rle_encode(data):
    if not data:
        return bytearray()
    
    result = bytearray()
    count = 1
    current = data[0]
    
    for i in range(1, len(data)):
        val = data[i]
        if val == current and count < 255:
            count += 1
        else:
            result.append(current)
            result.append(count)
            current = val
            count = 1
    
    result.append(current)
    result.append(count)
    
    return result

def rle_decode(data):
    if not data or len(data) % 2 != 0:
        raise ValueError("Invalid encoded data")
    
    result = bytearray()
    for i in range(0, len(data), 2):
        value = data[i]
        count = data[i + 1]
        result.extend([value] * count)
        
    return result

if __name__ == '__main__':
    original = bytearray([1, 1, 1, 2, 2, 3, 3, 3, 3])
    encoded = rle_encode(original)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)