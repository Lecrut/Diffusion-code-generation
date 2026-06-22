def compress_integer_list(data):
    if not data:
        return []
    
    compressed = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1
    
    compressed.append((current_value, count))
    return compressed

def decompress_integer_list(compressed_data):
    if not compressed_data:
        return []
    
    original = []
    for value, count in compressed_data:
        original.extend([value] * count)
    
    return original

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
    encoded = compress_integer_list(sample_input)
    print(encoded)
    decoded = decompress_integer_list(encoded)
    print(decoded)