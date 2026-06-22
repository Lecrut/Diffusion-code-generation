def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = data[i]
            count = 1
    
    if count > 1:
        encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

def rle_decode(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    
    decoded_parts = []
    i = 0
    n = len(encoded_data)
    
    while i < n:
        if encoded_data[i].isdigit():
            count = 0
            while i < n and encoded_data[i].isdigit():
                count = count * 10 + int(encoded_data[i])
                i += 1
            char = encoded_data[i]
            decoded_parts.append(char * count)
            i += 1
        else:
            decoded_parts.append(encoded_data[i])
            i += 1
    
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_data = "AAABBBCCCCD"
    encoded = rle_encode(sample_data)
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)
    
    sample_data2 = "XYZ"
    encoded2 = rle_encode(sample_data2)
    print(encoded2)
    
    decoded2 = rle_decode(encoded2)
    print(decoded2)
    
    sample_data3 = "AABBCCDD"
    encoded3 = rle_encode(sample_data3)
    print(encoded3)
    
    decoded3 = rle_decode(encoded3)
    print(decoded3)