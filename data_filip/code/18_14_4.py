def run_length_encode(data: str) -> list:
    if not data:
        return []
    
    encoded = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)