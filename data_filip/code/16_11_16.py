def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return ''.join(result)

if __name__ == '__main__':
    samples = [
        "",
        "a",
        "aaa",
        "aabbbcc",
        "abc",
        "aabbcc",
        "aaabbbccc",
        "aabbbaaccc",
        "hello world",
        "111222333"
    ]
    for sample in samples:
        print(run_length_encode(sample))