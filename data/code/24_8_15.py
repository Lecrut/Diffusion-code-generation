def rle_compression(data):
    if not data:
        return ("", 0.0)
    
    if len(data) == 0:
        return ("", 0.0)
    
    compressed = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(f"{count}{current_char}")
            else:
                compressed.append(current_char)
            current_char = data[i]
            count = 1
    
    if count > 1:
        compressed.append(f"{count}{current_char}")
    else:
        compressed.append(current_char)
    
    compressed_str = "".join(compressed)
    original_size = len(data)
    compressed_size = len(compressed_str)
    
    if original_size == 0:
        ratio = 0.0
    else:
        ratio = (1 - (compressed_size / original_size)) * 100
    
    return (compressed_str, ratio)

if __name__ == '__main__':
    sample_data = "A" * 500 + "B" * 300 + "C" * 200
    compressed, ratio = rle_compression(sample_data)
    print(compressed)
    print(ratio)