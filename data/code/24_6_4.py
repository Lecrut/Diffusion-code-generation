import itertools

def rle_compress(text):
    if not text:
        return ""
    compressed = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        compressed.append(f"{count}{char}")
    return "".join(compressed)

def rle_decompress(text):
    if not text:
        return ""
    decompressed = []
    i = 0
    while i < len(text):
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1
        if i < len(text):
            char = text[i]
            count = int(num_str)
            decompressed.append(char * count)
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_data = rle_compress(sample_input)
    decompressed_data = rle_decompress(compressed_data)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed_data}")
    print(f"Decompressed: {decompressed_data}")
    print(f"Round-trip successful: {sample_input == decompressed_data}")