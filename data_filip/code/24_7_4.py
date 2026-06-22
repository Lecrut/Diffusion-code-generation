def rle_compress(data):
    if not data:
        return ""
    if len(data) == 1:
        return "1" + data
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def rle_decompress(data):
    if not data:
        return ""
    result = []
    for i in range(0, len(data), 2):
        count = int(data[i])
        char = data[i + 1]
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original = "0011100"
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    
    original2 = "AAAAABBBCC"
    compressed2 = rle_compress(original2)
    decompressed2 = rle_decompress(compressed2)
    print(f"Original: {original2}")
    print(f"Compressed: {compressed2}")
    print(f"Decompressed: {decompressed2}")
    
    original3 = ""
    compressed3 = rle_compress(original3)
    decompressed3 = rle_decompress(compressed3)
    print(f"Original: '{original3}'")
    print(f"Compressed: '{compressed3}'")
    print(f"Decompressed: '{decompressed3}'")
    
    original4 = "A"
    compressed4 = rle_compress(original4)
    decompressed4 = rle_decompress(compressed4)
    print(f"Original: '{original4}'")
    print(f"Compressed: '{compressed4}'")
    print(f"Decompressed: '{decompressed4}'")