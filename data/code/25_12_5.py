def encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[-1])
    return "".join(result)

def decode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        count = int(s[i:j])
        result.append(s[j] * count)
        i = j + 1
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCCCDDDDEEEEFFFFFGGGGHHHIIJJ"
    encoded = encode(original)
    decoded = decode(encoded)
    print(encoded)
    print(decoded)
    print("Match: " + str(original == decoded))