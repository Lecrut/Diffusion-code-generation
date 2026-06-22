def enhanced_rle_encode(data):
    if not data:
        return ""
    
    escape_char = '\\'
    count_prefix = 'C'
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        
        while i + count < n and data[i + count] == current_char and count < 255:
            count += 1
        
        if current_char == escape_char:
            result.append(escape_char + escape_char)
            i += 1
        elif current_char == count_prefix:
            result.append(escape_char + count_prefix)
            i += 1
        elif count > 3:
            result.append(count_prefix)
            result.append(str(count))
            result.append(current_char)
            i += count
        else:
            for _ in range(count):
                if current_char == escape_char:
                    result.append(escape_char + escape_char)
                else:
                    result.append(current_char)
            i += count
    
    return ''.join(result)

def enhanced_rle_decode(data):
    escape_char = '\\'
    count_prefix = 'C'
    
    result = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        
        if current_char == escape_char:
            if i + 1 < n:
                result.append(data[i + 1])
                i += 2
            else:
                i += 1
        elif current_char == count_prefix:
            if i + 1 < n and data[i + 1].isdigit():
                count_str = ""
                j = i + 1
                while j < n and data[j].isdigit():
                    count_str += data[j]
                    j += 1
                count = int(count_str)
                if j < n:
                    result.append(data[j] * count)
                    i = j + 1
                else:
                    i = n
            else:
                result.append(count_prefix)
                i += 1
        else:
            result.append(current_char)
            i += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDaa\\bC5escape"
    encoded = enhanced_rle_encode(sample_data)
    decoded = enhanced_rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(decoded == sample_data)