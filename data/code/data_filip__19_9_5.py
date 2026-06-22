def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        current_char = data[i]
        run_count = 1
        
        while i + run_count < length and data[i + run_count] == current_char:
            run_count += 1
        
        if run_count > 3 and current_char not in '\\0123456789':
            result.append(f"{run_count}{current_char}")
        else:
            for _ in range(run_count):
                if current_char in '\\0123456789':
                    result.append(f"\\{current_char}")
                else:
                    result.append(current_char)
        
        i += run_count
    
    return "".join(result)

def rle_decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        if i + 1 < length and data[i] == '\\':
            if i + 1 < length:
                result.append(data[i + 1])
                i += 2
                continue
            else:
                result.append(data[i])
                i += 1
                continue
        
        count_str = ""
        while i < length and data[i].isdigit():
            count_str += data[i]
            i += 1
        
        if count_str and i < length:
            count = int(count_str)
            char = data[i]
            result.append(char * count)
            i += 1
        elif count_str:
            raise ValueError("Invalid RLE format: count without character")
        else:
            result.append(data[i])
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCCD"
    encoded = rle_encode(sample)
    decoded = rle_decode(encoded)
    
    print(encoded)
    print(decoded)
    print(decoded == sample)