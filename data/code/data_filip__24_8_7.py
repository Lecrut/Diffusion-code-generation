def rle_compress(text: str) -> tuple[str, float]:
    if not text:
        return ("", 1.0)
    
    compressed = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(f"{count}{current_char}")
            else:
                compressed.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        compressed.append(f"{count}{current_char}")
    else:
        compressed.append(current_char)
    
    compressed_str = "".join(compressed)
    ratio = len(text) / len(compressed_str) if compressed_str else 1.0
    
    return (compressed_str, ratio)

if __name__ == '__main__':
    original_string = "A" * 300 + "B" * 200 + "C" * 150 + "D" * 100 + "E" * 100 + "F" * 100 + "G" * 50

    compressed_text, compression_ratio = rle_compress(original_string)

    print(compressed_text)
    print(compression_ratio)