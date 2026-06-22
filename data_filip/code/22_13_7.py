def rle_compress_twist(data: str) -> str:
    if not data:
        return ""
    
    result = []
    n = len(data)
    i = 0
    
    while i < n:
        current_char = data[i]
        count = 1
        while i + count < n and data[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(f"{count}{current_char}")
            i += count
        else:
            result.append(current_char)
            i += 1
            
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    compressed = rle_compress_twist(sample_data)
    print(compressed)