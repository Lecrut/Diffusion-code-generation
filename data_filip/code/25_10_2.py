def compress_string(s):
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
    compressed_result = "".join(compressed)
    return compressed_result if len(compressed_result) < len(s) else s

if __name__ == '__main__':
    sample_input = "aaabbbccccdddd"
    result = compress_string(sample_input)
    print(result)
    sample_input_empty = ""
    result_empty = compress_string(sample_input_empty)
    print(result_empty)
    sample_input_single = "a"
    result_single = compress_string(sample_input_single)
    print(result_single)
    sample_input_mixed = "aabbbaaccc"
    result_mixed = compress_string(sample_input_mixed)
    print(result_mixed)