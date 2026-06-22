def rle_compress(data: str) -> tuple:
    if not data:
        return "", 1.0
    compressed_parts = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    compressed_parts.append(f"{current_char}{count}")
    compressed_string = "".join(compressed_parts)
    original_length = len(data)
    compressed_length = len(compressed_string)
    ratio = original_length / compressed_length if compressed_length > 0 else 0.0
    return compressed_string, ratio

if __name__ == "__main__":
    sample_input = "A" * 100 + "B" * 200 + "C" * 150 + "D" * 50 + "E" * 250 + "F" * 100 + "G" * 100 + "H" * 50
    result_string, ratio_value = rle_compress(sample_input)
    print(f"{result_string}")
    print(f"{ratio_value}")