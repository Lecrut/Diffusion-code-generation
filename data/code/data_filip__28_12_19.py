def run_length_compress(data):
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    sample_data = ['A', 'A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C']
    compressed = run_length_compress(sample_data)
    print(compressed)