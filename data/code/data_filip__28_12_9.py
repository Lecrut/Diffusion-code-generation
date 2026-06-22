def run_length_compress(chars):
    if not chars:
        return []
    
    compressed = []
    current_char = chars[0]
    count = 1
    
    for char in chars[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a', 'a']
    result = run_length_compress(sample_chars)
    print(result)