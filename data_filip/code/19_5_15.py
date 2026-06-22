def rle_encode(data, max_run):
    if not data:
        return []
    
    if max_run <= 0:
        raise ValueError("max_run must be positive")
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char and count < max_run:
            count += 1
        else:
            encoded.append((current_char, count))
            if data[i] != current_char:
                current_char = data[i]
                count = 1
            else:
                current_char = data[i]
                count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_data = "AAABBBBBBBBCCCCCCC"
    limit = 5
    result = rle_encode(sample_data, limit)
    print(result)