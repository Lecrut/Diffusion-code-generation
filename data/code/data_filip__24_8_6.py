def rle_compress(data):
    if not data:
        return "", 0.0
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 255:
            count += 1
        else:
            compressed.append((count, current_char))
            current_char = char
            count = 1
    compressed.append((count, current_char))
    compressed_str = "".join(f"{count}{char}" for count, char in compressed)
    original_length = len(data)
    compressed_length = len(compressed_str)
    ratio = compressed_length / original_length if original_length > 0 else 0
    return compressed_str, ratio

def generate_sample_data(length=1000):
    seed = "ABBC"
    result = []
    for i in range(length):
        result.append(seed[i % len(seed)])
    return "".join(result)

if __name__ == '__main__':
    sample_string = generate_sample_data(1000)
    compressed, ratio = rle_compress(sample_string)
    print(compressed)
    print(ratio)