def compress_string(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1
    compressed.append(current_char + str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample = "aabcccccaaa"
    print(compress_string(sample))
    sample_empty = ""
    print(compress_string(sample_empty))
    sample_single = "a"
    print(compress_string(sample_single))
    sample_no_run = "abc"
    print(compress_string(sample_no_run))
    sample_all_same = "zzzzz"
    print(compress_string(sample_all_same))