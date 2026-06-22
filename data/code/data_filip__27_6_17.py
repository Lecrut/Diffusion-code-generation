def rle_encode(s):
    if not s:
        return []
    
    byte_array = s.encode('utf-8')
    result = []
    current_byte = byte_array[0]
    count = 1
    
    for i in range(1, len(byte_array)):
        if byte_array[i] == current_byte:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = byte_array[i]
            count = 1
    
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    sample = "AAABBBCCCDAA"
    print(rle_encode(sample))