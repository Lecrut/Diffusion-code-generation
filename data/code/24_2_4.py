def rle_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def rle_decode(data):
    decoded = []
    for char, count in data:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == "__main__":
    original = "AAABBBCCCCDDDDDDD"
    compressed = rle_encode(original)
    decompressed = rle_decode(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Fidelity Check: {original == decompressed}")

    original_2 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_2 = rle_encode(original_2)
    decompressed_2 = rle_decode(compressed_2)
    print(f"Original 2: {original_2}")
    print(f"Compressed 2: {compressed_2}")
    print(f"Decompressed 2: {decompressed_2}")
    print(f"Fidelity Check 2: {original_2 == decompressed_2}")