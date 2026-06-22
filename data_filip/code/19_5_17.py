def rle_encode(data, max_run_length):
    if not data:
        return []
    
    if max_run_length <= 0:
        raise ValueError("max_run_length must be greater than 0")
    
    encoded = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        count = 1
        i += 1
        
        while i < n and data[i] == current_char and count < max_run_length:
            count += 1
            i += 1
        
        if count > max_run_length:
            full_runs = count // max_run_length
            remainder = count % max_run_length
            
            for _ in range(full_runs):
                encoded.append((current_char, max_run_length))
            
            if remainder > 0:
                encoded.append((current_char, remainder))
        else:
            encoded.append((current_char, count))
    
    return encoded

if __name__ == '__main__':
    sample_data = "A" * 25 + "B" * 10 + "C"
    max_run = 5
    result = rle_encode(sample_data, max_run)
    print(result)