def rle_compress(data: str) -> tuple:
    if not data:
        return "", 0.0
    
    compressed_parts = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    compressed_parts.append(f"{current_char}{count}")
    compressed_string = "".join(compressed_parts)
    compression_ratio = len(compressed_string) / len(data)
    
    return compressed_string, compression_ratio

if __name__ == "__main__":
    sample_string = "A" * 200 + "BC" * 300 + "XYZ" * 100
    result_string, ratio = rle_compress(sample_string)
    print(f"Compressed: {result_string}")
    print(f"Compression Ratio: {ratio}")