def rle_compress(data):
    if not data:
        return ""
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(current_char)
            current_char = data[i]
            count = 1
    
    compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

def rle_decompress(compressed):
    if not compressed:
        return ""
    
    decompressed = []
    i = 0
    while i < len(compressed):
        if not compressed[i].isdigit():
            raise ValueError("Invalid compressed format: expected digit at position {}".format(i))
        
        num_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            num_str += compressed[i]
            i += 1
        
        if i >= len(compressed):
            raise ValueError("Invalid compressed format: expected character after count")
        
        count = int(num_str)
        char = compressed[i]
        decompressed.append(char * count)
        i += 1
    
    return "".join(decompressed)

if __name__ == '__main__':
    sample_data = '0011100'
    compressed = rle_compress(sample_data)
    decompressed = rle_decompress(compressed)
    
    print("Original:  {}".format(sample_data))
    print("Compressed: {}".format(compressed))
    print("Decompressed: {}".format(decompressed))
    print("Match: {}".format(sample_data == decompressed))
    
    empty_data = ''
    compressed_empty = rle_compress(empty_data)
    decompressed_empty = rle_decompress(compressed_empty)
    print("Empty Original:  '{}'".format(empty_data))
    print("Empty Compressed: '{}'".format(compressed_empty))
    print("Empty Decompressed: '{}'".format(decompressed_empty))
    print("Empty Match: {}".format(empty_data == decompressed_empty))
    
    single_char = '1'
    compressed_single = rle_compress(single_char)
    decompressed_single = rle_decompress(compressed_single)
    print("Single Original:  '{}'".format(single_char))
    print("Single Compressed: '{}'".format(compressed_single))
    print("Single Decompressed: '{}'".format(decompressed_single))
    print("Single Match: {}".format(single_char == decompressed_single))