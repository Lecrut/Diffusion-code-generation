def rle_compress(data: str) -> str:
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    compressed.append(f"{count}{current_char}")
    return "".join(compressed)

def calculate_ratio(original_len: int, compressed_len: int) -> float:
    if original_len == 0:
        return 1.0
    return original_len / compressed_len

def process_rle(original_string: str):
    compressed_string = rle_compress(original_string)
    ratio = calculate_ratio(len(original_string), len(compressed_string))
    return compressed_string, ratio

if __name__ == '__main__':
    data = "A" * 500 + "B" * 500
    compressed, ratio = process_rle(data)
    print((compressed, ratio))