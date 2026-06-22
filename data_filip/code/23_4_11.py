def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    decoded = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            count = int(num_str)
            if i < len(s):
                char = s[i]
                decoded.append(char * count)
                i += 1
        else:
            decoded.append(s[i])
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    test_strings = [
        "AABBBCCCC",
        "Hello World",
        "AAAAABBBCC",
        "XYZ",
        "",
        "A",
        "AAAAAAAAAAABBBBBBBBCCCCCDDDD"
    ]
    for s in test_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()