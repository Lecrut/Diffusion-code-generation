def bidirectional_rle_processing(text):
    def compress(s):
        if not s:
            return ""
        compressed = []
        count = 1
        char = s[0]
        for i in range(1, len(s)):
            if s[i] == char:
                count += 1
            else:
                compressed.append(f"{count}{char}")
                char = s[i]
                count = 1
        compressed.append(f"{count}{char}")
        return "".join(compressed)

    def decompress(s):
        if not s:
            return ""
        decompressed = []
        i = 0
        while i < len(s):
            count = 0
            while i < len(s) and s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            if i < len(s):
                char = s[i]
                decompressed.append(char * count)
                i += 1
        return "".join(decompressed)

    compressed = compress(text)
    decompressed = decompress(compressed)
    integrity_check = (text == decompressed)
    return {
        "original": text,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity_check": integrity_check
    }

if __name__ == '__main__':
    sample_text = "aaabbcccc"
    result = bidirectional_rle_processing(sample_text)
    print(result)