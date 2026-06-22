def rle_compress(data: str) -> tuple:
    if not data:
        return "", 1.0
    
    compressed_parts = []
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_parts.append(f"{count}{data[i - 1]}")
            count = 1
    
    compressed_parts.append(f"{count}{data[-1]}")
    compressed_str = "".join(compressed_parts)
    
    original_len = len(data)
    compressed_len = len(compressed_str)
    ratio = original_len / compressed_len if compressed_len > 0 else 0.0
    
    return compressed_str, ratio

if __name__ == "__main__":
    sample_string = "A" * 500 + "B" * 300 + "C" * 200
    result_compressed, result_ratio = rle_compress(sample_string)
    print(result_compressed)
    print(result_ratio)