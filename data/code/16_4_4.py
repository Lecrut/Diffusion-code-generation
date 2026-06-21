def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    compressed.append(current_char + str(count))
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbccccdeeee"
    result = compress_string(sample_input)
    print(result)
    another_sample = "zzzz"
    print(compress_string(another_sample))
    empty_sample = ""
    print(compress_string(empty_sample))
    mixed_sample = "a1b2c3"
    print(compress_string(mixed_sample))