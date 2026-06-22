def run_length_encode(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == "__main__":
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaaaa"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aabbbcccc"))