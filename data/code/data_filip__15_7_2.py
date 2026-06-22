def compress_string(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbbccc"
    compressed = compress_string(sample_input)
    print(compressed)