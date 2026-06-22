def rle_compress(data: str) -> tuple[str, float]:
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
    
    compressed.append(f"{data[length - 1]}{count}")
    
    compressed_str = "".join(compressed)
    ratio = len(compressed_str) / length
    
    return compressed_str, ratio

if __name__ == "__main__":
    sample_string = "A" * 100 + "B" * 100 + "C" * 100 + "D" * 100 + "E" * 100 + "F" * 100 + "G" * 100 + "H" * 100 + "I" * 100 + "J" * 100
    result_string, result_ratio = rle_compress(sample_string)
    print(result_string)
    print(result_ratio)