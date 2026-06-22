def rle_compress(s: str) -> str:
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    print(rle_compress("aabcccccaaa"))
    print(rle_compress("abc"))
    print(rle_compress("a"))
    print(rle_compress("aa"))
    print(rle_compress(""))