def rle_compress(text):
    if not text:
        return '', 1.0
    
    compressed = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    compressed.append(f"{count}{current_char}")
    
    compressed_str = ''.join(compressed)
    ratio = len(text) / len(compressed_str) if len(compressed_str) > 0 else 0.0
    return compressed_str, ratio

if __name__ == '__main__':
    sample_string = 'A' * 500 + 'B' * 300 + 'C' * 200
    result, ratio = rle_compress(sample_string)
    print(f"Compressed: {result}")
    print(f"Ratio: {ratio}")