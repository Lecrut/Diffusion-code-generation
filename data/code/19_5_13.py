def rle_encode_with_limit(data: str, max_run: int = 255) -> str:
    if not data:
        return ""
    
    if max_run < 1:
        raise ValueError("max_run must be at least 1")
    
    encoded = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char and count < max_run:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_data = "AAABBBCCCAA"
    max_run = 2
    
    result = rle_encode_with_limit(sample_data, max_run)
    print(result)