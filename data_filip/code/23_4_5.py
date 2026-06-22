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
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        if i < len(encoded):
            char = encoded[i]
            i += 1
            decoded.append(char * int(num_str))
    return "".join(decoded)

if __name__ == '__main__':
    samples = [
        "AABCCCDD",
        "AAAAAAAAAA",
        "Hello World!!!",
        "",
        "A",
        "AABBCC",
        "abcdef"
    ]
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: '{sample}' -> Encoded: '{encoded}' -> Decoded: '{decoded}'")