def run_length_encode(s):
    if not s:
        return s
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1])
            if count > 1:
                encoded.append(str(count))
            count = 1
    encoded.append(s[-1])
    if count > 1:
        encoded.append(str(count))
    result = ''.join(encoded)
    if len(result) >= len(s):
        return s
    return result

if __name__ == '__main__':
    samples = ["", "A", "AA", "AAB", "AABB", "AAAABBBCCDAA", "ABC", "AAAAAAAAA"]
    for sample in samples:
        print(run_length_encode(sample))