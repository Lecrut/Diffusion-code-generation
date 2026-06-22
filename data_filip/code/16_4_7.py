def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    compressed_output = compress_string(sample_input)
    print(compressed_output)
    empty_string = ""
    empty_result = compress_string(empty_string)
    print(empty_result)
    single_char = "z"
    single_result = compress_string(single_char)
    print(single_result)