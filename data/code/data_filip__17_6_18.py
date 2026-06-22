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
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    test_input = "aaabbbccccdddd"
    output = compress_string(test_input)
    print(output)
    test_input_empty = ""
    output_empty = compress_string(test_input_empty)
    print(output_empty)
    test_input_single = "z"
    output_single = compress_string(test_input_single)
    print(output_single)
    test_input_mixed = "AABBCCDD112233"
    output_mixed = compress_string(test_input_mixed)
    print(output_mixed)