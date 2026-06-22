def rle_encode_with_limit(data, max_run):
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
            if count == max_run:
                result.append((current_char, count))
                current_char = char
                count = 0
        else:
            if count > 0:
                result.append((current_char, count))
            current_char = char
            count = 1
    
    if count > 0:
        result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    max_run_length = 3
    encoded = rle_encode_with_limit(sample_data, max_run_length)
    print(encoded)