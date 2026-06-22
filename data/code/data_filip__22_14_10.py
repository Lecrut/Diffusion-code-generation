def rle_compress(s: str) -> str:
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return "".join(compressed)

def compare_and_compress(s: str) -> str:
    if not s:
        return s
    compressed = rle_compress(s)
    return compressed if len(compressed) < len(s) else s

if __name__ == "__main__":
    sample_string = "AAAABBBCCDAA"
    result = compare_and_compress(sample_string)
    print(result)
    sample_string_2 = "A"
    result_2 = compare_and_compress(sample_string_2)
    print(result_2)
    sample_string_3 = "AABBCC"
    result_3 = compare_and_compress(sample_string_3)
    print(result_3)