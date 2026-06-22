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
    return "".join(result)

def run_length_decode(s):
    result = []
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        if i < len(s):
            char = s[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "",
        "a",
        "aaa",
        "aabbbcccd",
        "aabbccddeeff",
        "xyzzzxxxxxyyyyy",
        "1233344445",
        "hello world"
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded: {encoded!r}")
        print(f"Decoded: {decoded!r}")
        print(f"Match: {s == decoded}")
        print("-" * 40)