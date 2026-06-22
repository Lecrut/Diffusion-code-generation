def rle_encode(data: str, max_run: int = 1) -> list:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
            if count == max_run:
                result.append((count, current_char))
                current_char = ""
                count = 0
        else:
            if count > 0:
                result.append((count, current_char))
            current_char = char
            count = 1
            
    if count > 0:
        result.append((count, current_char))
        
    return result

if __name__ == '__main__':
    sample_text = "AAABBBCC"
    max_length = 2
    encoded_output = rle_encode(sample_text, max_length)
    print(encoded_output)