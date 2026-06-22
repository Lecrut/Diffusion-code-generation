def run_length_encode(text):
    if not text:
        return "", 1.0
    compressed_parts = []
    count = 1
    length = len(text)
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed_parts.append(f"{text[i - 1]}{count}")
            count = 1
    compressed_parts.append(f"{text[-1]}{count}")
    compressed_string = "".join(compressed_parts)
    compression_ratio = len(text) / len(compressed_string)
    return compressed_string, compression_ratio

if __name__ == '__main__':
    sample_data = "A" * 100 + "B" * 200 + "C" * 150 + "D" * 50 + "E" * 100 + "F" * 200 + "G" * 50 + "H" * 100 + "I" * 50
    result_string, result_ratio = run_length_encode(sample_data)
    print(f"{result_string}")
    print(f"{result_ratio}")