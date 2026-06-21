def run_length_encode(s):
    if not s:
        return {}
    
    filtered = [c for c in s if c.isalnum()]
    if not filtered:
        return {}
    
    result = []
    current_char = filtered[0]
    count = 1
    
    for i in range(1, len(filtered)):
        if filtered[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = filtered[i]
            count = 1
    
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    sample_input = "AAABBC1122"
    encoded = run_length_encode(sample_input)
    print(encoded)