def rle_compress(data):
    if not data:
        return "", 0.0

    compressed = []
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = data[i]
            count = 1

    compressed.append(str(count) + current_char)
    compressed_string = "".join(compressed)

    original_length = len(data)
    compressed_length = len(compressed_string)
    ratio = original_length / compressed_length if compressed_length > 0 else 0.0

    return compressed_string, ratio

def generate_hardcoded_string(length):
    import string
    import random
    random.seed(42)
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    hardcoded_string = generate_hardcoded_string(1000)
    compressed_str, compression_ratio = rle_compress(hardcoded_string)
    print(compressed_str)
    print(compression_ratio)