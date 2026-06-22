def rle_compress(s):
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

def compress_if_beneficial(s):
    if not s:
        return s
    compressed = rle_compress(s)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample_input_1 = "AAAAABBBCC"
    sample_input_2 = "ABC"
    sample_input_3 = "A"
    result_1 = compress_if_beneficial(sample_input_1)
    result_2 = compress_if_beneficial(sample_input_2)
    result_3 = compress_if_beneficial(sample_input_3)
    print(result_1)
    print(result_2)
    print(result_3)