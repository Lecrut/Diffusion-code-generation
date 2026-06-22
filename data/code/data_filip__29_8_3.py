def encode_consecutive_repeats(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(s[i - 1])
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(s[-1])
    return "".join(encoded)

if __name__ == "__main__":
    print(encode_consecutive_repeats("aabbcccc"))
    print(encode_consecutive_repeats("abc"))
    print(encode_consecutive_repeats("aaabbbcc"))
    print(encode_consecutive_repeats(""))
    print(encode_consecutive_repeats("x"))
    print(encode_consecutive_repeats("xxxxx"))
    print(encode_consecutive_repeats("aabbbcccc"))