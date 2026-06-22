def run_length_encode(data):
    if not data:
        return []
    
    result = []
    iterator = iter(data)
    
    current_char = next(iterator)
    count = 1
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    sample_input = "aabbbcccc"
    encoded = run_length_encode(sample_input)
    print(encoded)