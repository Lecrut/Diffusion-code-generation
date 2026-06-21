def rle_roundtrip(s):
    compressed = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        while i + count < len(s) and s[i + count] == char:
            count += 1
        compressed.append(f"{count}{char}")
        i += count
    compressed_str = "".join(compressed)
    decompressed = []
    j = 0
    while j < len(compressed_str):
        num_str = ""
        while j < len(compressed_str) and compressed_str[j].isdigit():
            num_str += compressed_str[j]
            j += 1
        if num_str and j < len(compressed_str):
            count = int(num_str)
            char = compressed_str[j]
            decompressed.append(char * count)
            j += 1
    return "".join(decompressed)

if __name__ == '__main__':
    sample = "AAABBBCCCD"
    print(rle_roundtrip(sample))