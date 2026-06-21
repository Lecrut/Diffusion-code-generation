def run_length_encode(data):
    if not data:
        return {}
    
    counts = {}
    current_char = data[0]
    current_count = 1
    
    for char in data[1:]:
        if char == current_char:
            current_count += 1
        else:
            counts[current_char] = current_count
            current_char = char
            current_count = 1
    counts[current_char] = current_count
    return counts

if __name__ == '__main__':
    sample_text = "aabccca"
    result = run_length_encode(sample_text)
    print(result)