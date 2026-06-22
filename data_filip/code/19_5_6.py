def rle_encode_constrained(data: str, max_run_length: int) -> list:
    if not data or max_run_length <= 0:
        return []
    
    encoded_segments = []
    n = len(data)
    i = 0
    
    while i < n:
        current_char = data[i]
        count = 1
        while i + count < n and data[i + count] == current_char and count < max_run_length:
            count += 1
        encoded_segments.append(f"{count}{current_char}")
        i += count
        
    return encoded_segments

if __name__ == '__main__':
    sample_data = "AAAAAAAAAAAAAAAAAAAAAA"
    max_len = 5
    result = rle_encode_constrained(sample_data, max_len)
    print(result)