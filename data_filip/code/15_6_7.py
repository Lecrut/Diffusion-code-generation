def compress_sequence(sequence):
    if not sequence:
        return []
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    
    return result

def decompress_sequence(pairs):
    result = []
    for char, count in pairs:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    original = 'zzzzzxyyy'
    compressed = compress_sequence(original)
    decompressed = decompress_sequence(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Lossless: {original == decompressed}")