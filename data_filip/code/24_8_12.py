def rle_compress(data: str) -> tuple:
    if not data:
        return "", 0.0
    
    compressed_parts = []
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_parts.append(f"{data[i - 1]}{count}")
            count = 1
    
    compressed_parts.append(f"{data[-1]}{count}")
    compressed_string = "".join(compressed_parts)
    
    original_length = len(data)
    compressed_length = len(compressed_string)
    
    if compressed_length == 0:
        compression_ratio = 0.0
    else:
        compression_ratio = original_length / compressed_length
    
    return compressed_string, compression_ratio

if __name__ == "__main__":
    sample_data = "AAAAAAAAAA" * 100
    result_compressed, result_ratio = rle_compress(sample_data)
    print(result_compressed)
    print(result_ratio)