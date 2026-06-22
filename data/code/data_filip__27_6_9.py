def rle_encode(data: str) -> list[tuple[int, str]]:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    index = 1
    length = len(data)
    
    while index < length:
        char = data[index]
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
        index += 1
        
    result.append((count, current_char))
    
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded_result = rle_encode(sample_string)
    print(encoded_result)