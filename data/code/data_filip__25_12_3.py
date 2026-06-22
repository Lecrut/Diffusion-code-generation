def encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    prev = s[0]
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            encoded.append(str(count) + prev)
            count = 1
            prev = char
    encoded.append(str(count) + prev)
    return "".join(encoded)

def decode(s):
    if not s:
        return ""
    decoded = []
    i = 0
    while i < len(s):
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if i < len(s):
            count = int(num_str)
            char = s[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    original = "aaabbcdddd"
    compressed = encode(original)
    decompressed = decode(compressed)
    print(original)
    print(compressed)
    print(decompressed)