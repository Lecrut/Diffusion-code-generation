def rle_encode_with_max_run(data, max_run):
    if not data:
        return []
    
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        run_length = 1
        while i + run_length < len(data) and data[i + run_length] == current_char and run_length < max_run:
            run_length += 1
        
        result.append((current_char, run_length))
        i += run_length
    
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    max_run_length = 3
    encoded = rle_encode_with_max_run(sample_data, max_run_length)
    print(encoded)