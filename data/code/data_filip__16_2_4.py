def rle_encode(data):
    if not data:
        return []
    
    encoded = []
    current_byte = data[0]
    count = 1
    
    for byte in data[1:]:
        if byte == current_byte:
            count += 1
        else:
            encoded.append((current_byte, count))
            current_byte = byte
            count = 1
    
    encoded.append((current_byte, count))
    
    return encoded

if __name__ == '__main__':
    sample_data = b'AABBBCCCC'
    result = rle_encode(sample_data)
    print(result)