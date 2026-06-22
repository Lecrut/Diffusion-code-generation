def rle_compression(data):
    if not data:
        return "", 0.0

    compressed = []
    current_char = data[0]
    count = 1

    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1

    compressed.append((current_char, count))

    compressed_str = "".join(
        f"{char}{count}" for char, count in compressed
    )

    original_length = len(data)
    compressed_length = len(compressed_str)

    if original_length == 0:
        ratio = 0.0
    else:
        ratio = compressed_length / original_length

    return compressed_str, ratio

if __name__ == '__main__':
    sample_data = "A" * 300 + "B" * 250 + "C" * 200 + "D" * 150 + "E" * 100
    compressed, ratio = rle_compression(sample_data)
    print(compressed)
    print(ratio)