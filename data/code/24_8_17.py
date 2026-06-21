def rle_compress(data: str) -> tuple[str, float]:
    if not data:
        return ("", 0.0)
    
    compressed_parts = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed_parts.append(f"{count}{current_char}")
    
    compressed_string = "".join(compressed_parts)
    original_length = len(data)
    compressed_length = len(compressed_string)
    ratio = original_length / compressed_length if compressed_length > 0 else 0.0
    
    return (compressed_string, ratio)

if __name__ == '__main__':
    sample_string = "A" * 500 + "B" * 250 + "C" * 250
    result = rle_compress(sample_string)
    print(result)