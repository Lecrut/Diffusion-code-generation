def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    
    return "".join(result)

def rle_decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        count_str = []
        while i < length and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        count = int("".join(count_str))
        char = data[i]
        result.append(char * count)
        i += 1
        
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded = rle_encode(sample_input)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)