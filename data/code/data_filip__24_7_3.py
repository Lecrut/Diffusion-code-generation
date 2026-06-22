def rle_compress(data):
    if not data:
        return ''
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = data[i]
            count = 1
    
    compressed.append((current_char, count))
    
    result = []
    for char, count in compressed:
        result.append(str(count))
        result.append(char)
    
    return ''.join(result)

def rle_decompress(data):
    if not data:
        return ''
    
    decompressed = []
    i = 0
    
    while i < len(data):
        count_str = ''
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        
        if not count_str or i >= len(data):
            break
        
        count = int(count_str)
        char = data[i]
        i += 1
        
        decompressed.append(char * count)
    
    return ''.join(decompressed)

if __name__ == '__main__':
    original = '0011100'
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    
    print(original)
    print(compressed)
    print(decompressed)
    
    empty_original = ''
    empty_compressed = rle_compress(empty_original)
    empty_decompressed = rle_decompress(empty_compressed)
    
    print(empty_original)
    print(empty_compressed)
    print(empty_decompressed)
    
    single_original = '1'
    single_compressed = rle_compress(single_original)
    single_decompressed = rle_decompress(single_compressed)
    
    print(single_original)
    print(single_compressed)
    print(single_decompressed)
    
    complex_original = 'aaaaabbbccdddddd'
    complex_compressed = rle_compress(complex_original)
    complex_decompressed = rle_decompress(complex_compressed)
    
    print(complex_original)
    print(complex_compressed)
    print(complex_decompressed)