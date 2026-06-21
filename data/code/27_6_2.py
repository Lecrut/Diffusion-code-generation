def rle_encode(data: str) -> list:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    
    result.append((count, current_char))
    
    return result

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    encoded = rle_encode(sample_string)
    print(encoded)