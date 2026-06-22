import sys

def rle_compress(data: str) -> list:
    if not data:
        return []
    compressed = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = data[i]
            count = 1
    compressed.append((current_char, count))
    return compressed

def rle_decompress(compressed: list) -> str:
    if not compressed:
        return ""
    result = []
    for char, count in compressed:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_data = rle_compress(sample_text)
    decompressed_text = rle_decompress(compressed_data)
    print(compressed_data)
    print(decompressed_text)
    print(len(sample_text) - len(decompressed_text))