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
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        num_str = ""
        i += 1
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        count = int(num_str) if num_str else 1
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == "__main__":
    sample_strings = [
        "AAAABBBCCDAA",
        "ABCD",
        "AAAAAAAAA",
        "",
        "A"
    ]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r} -> Encoded: {encoded!r} -> Decoded: {decoded!r}")