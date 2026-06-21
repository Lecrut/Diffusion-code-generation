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
    if not s:
        return ""
    decoded = []
    i = 0
    while i < len(s):
        count_str = []
        while i < len(s) and s[i].isdigit():
            count_str.append(s[i])
            i += 1
        count = int("".join(count_str)) if count_str else 1
        char = s[i]
        i += 1
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample1 = "AAAABBBCCDAA"
    sample2 = "A"
    sample3 = ""
    sample4 = "AABBCC"
    encoded1 = run_length_encode(sample1)
    encoded2 = run_length_encode(sample2)
    encoded3 = run_length_encode(sample3)
    encoded4 = run_length_encode(sample4)
    decoded1 = run_length_decode(encoded1)
    decoded2 = run_length_decode(encoded2)
    decoded3 = run_length_decode(encoded3)
    decoded4 = run_length_decode(encoded4)
    print(encoded1)
    print(encoded2)
    print(encoded3)
    print(encoded4)
    print(decoded1)
    print(decoded2)
    print(decoded3)
    print(decoded4)