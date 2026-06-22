def compress_string(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    compressed.append(current_char + str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample_text = "aaabbccccdd"
    result = compress_string(sample_text)
    print(result)
    empty_text = ""
    empty_result = compress_string(empty_text)
    print(empty_result)
    single_char = "z"
    single_result = compress_string(single_char)
    print(single_result)
    mixed_text = "AaAa"
    mixed_result = compress_string(mixed_text)
    print(mixed_result)