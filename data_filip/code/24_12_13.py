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
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return "".join(char * count if count == 1 else str(count) + char for char, count in encoded)

def run_length_decode(s):
    decoded = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = 0
            while i < len(s) and s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            if i < len(s):
                decoded.append(s[i] * count)
                i += 1
        else:
            decoded.append(s[i])
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCD"
    compressed = run_length_encode(sample_string)
    print(sample_string)
    print(compressed)