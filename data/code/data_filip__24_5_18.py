def compress(data: str) -> str:
    if not data:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{data[i - 1]}")
            count = 1
    compressed.append(f"{count}{data[-1]}")
    return "".join(compressed)

def decompress(data: str) -> str:
    if not data:
        return ""
    decompressed = []
    count = 0
    for char in data:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count == 0:
                count = 1
            decompressed.append(char * count)
            count = 0
    return "".join(decompressed)

if __name__ == '__main__':
    original_text = "AAAAABBBCCDAA"
    encoded_text = compress(original_text)
    decoded_text = decompress(encoded_text)
    print(f"Original: {original_text}")
    print(f"Encoded: {encoded_text}")
    print(f"Decoded: {decoded_text}")
    print(f"Match: {original_text == decoded_text}")