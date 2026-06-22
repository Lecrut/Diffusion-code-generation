def rle_compress(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    compressed.append(current_char)
    compressed.append(str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample = "aaabbcddd"
    result = rle_compress(sample)
    print(result)