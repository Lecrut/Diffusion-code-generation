def run_length_compress(sequence):
    if not sequence:
        return []
    
    compressed = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    data = "aaabbcccdddeeefff"
    result = run_length_compress(data)
    print(result)