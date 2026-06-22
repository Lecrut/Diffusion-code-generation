def bidirectional_rle(s):
    def compress(text):
        if not text:
            return ""
        compressed = []
        count = 1
        current_char = text[0]
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                compressed.append(str(count))
                compressed.append(current_char)
                current_char = text[i]
                count = 1
        compressed.append(str(count))
        compressed.append(current_char)
        return "".join(compressed)

    def decompress(text):
        if not text:
            return ""
        decompressed = []
        i = 0
        while i < len(text):
            count = ""
            while i < len(text) and text[i].isdigit():
                count += text[i]
                i += 1
            if count:
                char = text[i]
                decompressed.append(char * int(count))
            i += 1
        return "".join(decompressed)

    compressed = compress(s)
    decompressed = decompress(compressed)
    return {
        "original": s,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity_check": s == decompressed
    }

if __name__ == '__main__':
    sample_string = "AAABBBCCCA"
    result = bidirectional_rle(sample_string)
    print(result)