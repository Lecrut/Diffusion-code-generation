def compress_run_length(data):
    if not data:
        return []
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
    result = compress_run_length(sample_input)
    print(result)