def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(s):
    decoded = []
    i = 0
    while i < len(s):
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        if i < len(s):
            char = s[i]
            i += 1
            decoded.append(char * int(count))
    return "".join(decoded)

if __name__ == '__main__':
    sample_strings = [
        "AAAABBBCCDAA",
        "ABC",
        "A",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()