def rle_compression(data):
    if not data:
        return "", 0.0
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    compressed_str = "".join(compressed)
    ratio = len(compressed_str) / len(data) if len(data) > 0 else 0.0
    return compressed_str, ratio

if __name__ == '__main__':
    import random
    import string
    random.seed(42)
    hardcoded_string = ''.join(random.choices('ABCD', k=1000))
    compressed_result, ratio_result = rle_compression(hardcoded_string)
    print(compressed_result)
    print(ratio_result)