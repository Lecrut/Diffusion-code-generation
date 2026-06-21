def bidirectional_rle(text):
    def compress(s):
        if not s:
            return ""
        result = []
        current_char = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = s[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(s):
        if not s:
            return ""
        result = []
        i = 0
        while i < len(s):
            count_str = ""
            while i < len(s) and s[i].isdigit():
                count_str += s[i]
                i += 1
            if i < len(s):
                char = s[i]
                i += 1
                count = int(count_str)
                result.append(char * count)
        return "".join(result)

    compressed = compress(text)
    decompressed = decompress(compressed)
    return {
        "original": text,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity_check": text == decompressed
    }

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    result = bidirectional_rle(sample_text)
    print(result)