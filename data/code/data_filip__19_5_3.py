def rle_with_max_run(data, max_run):
    if not data:
        return []
    if max_run < 1:
        raise ValueError("max_run must be at least 1")
    
    result = []
    i = 0
    while i < len(data):
        current_char = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_char and count < max_run:
            count += 1
        result.append((count, current_char))
        i += count
    
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    max_run_length = 2
    encoded = rle_with_max_run(sample_data, max_run_length)
    print(encoded)