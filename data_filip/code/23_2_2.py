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
                decoded.append(s[i] * count)
                i += 1
        else:
            decoded.append(s[i])
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample1 = "aabbbccccdeee"
    encoded1 = run_length_encode(sample1)
    print(encoded1)
    decoded1 = run_length_decode(encoded1)
    print(decoded1)

    sample2 = "abcdef"
    encoded2 = run_length_encode(sample2)
    print(encoded2)
    decoded2 = run_length_decode(encoded2)
    print(decoded2)

    sample3 = "aaabbaaac"
    encoded3 = run_length_encode(sample3)
    print(encoded3)
    decoded3 = run_length_decode(encoded3)
    print(decoded3)

    sample4 = ""
    encoded4 = run_length_encode(sample4)
    print(encoded4)
    decoded4 = run_length_decode(encoded4)
    print(decoded4)

    sample5 = "a"
    encoded5 = run_length_encode(sample5)
    print(encoded5)
    decoded5 = run_length_decode(encoded5)
    print(decoded5)