def enhanced_rle_encode(data):
    if not data:
        return ""
    
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_char and count < 255:
            count += 1
        
        if count == 1:
            if current_char == '\\' or current_char.isdigit():
                result.append('\\')
                result.append(current_char)
            else:
                result.append(current_char)
        else:
            result.append(str(count))
            if current_char == '\\' or current_char.isdigit():
                result.append('\\')
                result.append(current_char)
            else:
                result.append(current_char)
        
        i += count
    
    return ''.join(result)

def enhanced_rle_decode(encoded_data):
    if not encoded_data:
        return ""
    
    result = []
    i = 0
    while i < len(encoded_data):
        char = encoded_data[i]
        
        if char == '\\':
            if i + 1 < len(encoded_data):
                result.append(encoded_data[i + 1])
                i += 2
            else:
                result.append('\\')
                i += 1
        elif char.isdigit():
            count_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count_str += encoded_data[i]
                i += 1
            count = int(count_str)
            if i < len(encoded_data):
                next_char = encoded_data[i]
                if next_char == '\\' and i + 1 < len(encoded_data):
                    literal_char = encoded_data[i + 1]
                    result.append(literal_char * count)
                    i += 2
                else:
                    result.append(next_char * count)
                    i += 1
            else:
                i += 0
        else:
            result.append(char)
            i += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "AAABBBCCC"
    sample2 = "1234567890"
    sample3 = "\\^&*"
    sample4 = "AABBCCDD"
    sample5 = ""
    
    encoded1 = enhanced_rle_encode(sample1)
    decoded1 = enhanced_rle_decode(encoded1)
    print(decoded1)
    
    encoded2 = enhanced_rle_encode(sample2)
    decoded2 = enhanced_rle_decode(encoded2)
    print(decoded2)
    
    encoded3 = enhanced_rle_encode(sample3)
    decoded3 = enhanced_rle_decode(encoded3)
    print(decoded3)
    
    encoded4 = enhanced_rle_encode(sample4)
    decoded4 = enhanced_rle_decode(encoded4)
    print(decoded4)
    
    encoded5 = enhanced_rle_encode(sample5)
    decoded5 = enhanced_rle_decode(encoded5)
    print(decoded5)