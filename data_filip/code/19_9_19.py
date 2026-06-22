def enhanced_rle_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    n = len(data)
    escape_char = '~'
    count_prefix = '['
    
    i = 0
    while i < n:
        char = data[i]
        
        if char == escape_char or char == count_prefix or count_prefix in char:
            result.append(escape_char)
            result.append(char)
            count = 1
            i += 1
            continue
        
        if i + 1 < n and data[i + 1] == char:
            count += 1
            i += 1
        else:
            if count > 1:
                result.append(str(count))
                result.append(count_prefix)
                result.append(char)
            else:
                result.append(char)
            count = 1
            i += 1
            
    return "".join(result)

def enhanced_rle_decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    n = len(data)
    escape_char = '~'
    count_prefix = '['
    
    while i < n:
        char = data[i]
        
        if char == escape_char:
            if i + 1 < n:
                result.append(data[i + 1])
                i += 2
            else:
                result.append(escape_char)
                i += 1
            continue
        
        if char == count_prefix:
            count_str = ""
            i += 1
            while i < n and data[i].isdigit():
                count_str += data[i]
                i += 1
            if count_str:
                repeat_count = int(count_str)
                if i < n:
                    char = data[i]
                    result.append(char * repeat_count)
                    i += 1
            continue
        
        result.append(char)
        i += 1
        
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCC~~A1"
    encoded = enhanced_rle_encode(original)
    decoded = enhanced_rle_decode(encoded)
    
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {original == decoded}")
    
    sample2 = "XX[YYY~ZZZ"
    encoded2 = enhanced_rle_encode(sample2)
    decoded2 = enhanced_rle_decode(encoded2)
    
    print(f"\nOriginal: {sample2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")
    print(f"Match: {sample2 == decoded2}")