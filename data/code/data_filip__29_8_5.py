def encode_repeating_characters(s):
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

if __name__ == '__main__':
    sample1 = "aaabbc"
    print(encode_repeating_characters(sample1))
    sample2 = "abc"
    print(encode_repeating_characters(sample2))
    sample3 = "aaaaa"
    print(encode_repeating_characters(sample3))
    sample4 = ""
    print(encode_repeating_characters(sample4))
    sample5 = "aabbbccccd"
    print(encode_repeating_characters(sample5))