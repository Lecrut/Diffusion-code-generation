def rle_compress(data):
    if not data:
        return "", 0.0
    
    compressed = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count}")
            count = 1
    
    compressed.append(f"{data[-1]}{count}")
    compressed_str = "".join(compressed)
    
    ratio = len(compressed_str) / length
    return compressed_str, ratio

if __name__ == '__main__':
    sample_data = "AAABBBCCCCDDDDDDDEEEEEFFFFGGGGHHH" * 30 + "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
    compressed_output, compression_ratio = rle_compress(sample_data)
    print(compressed_output)
    print(compression_ratio)