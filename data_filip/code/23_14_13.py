def run_length_encoding(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            encoded.append(f"{count}{s[i-1]}")
            count = 1
    encoded.append(f"{count}{s[-1]}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_1 = "aaabbc"
    sample_2 = "AAAAA"
    sample_3 = ""
    sample_4 = "a1b2c3"
    sample_5 = "zzzzzzzz"
    print(run_length_encoding(sample_1))
    print(run_length_encoding(sample_2))
    print(run_length_encoding(sample_3))
    print(run_length_encoding(sample_4))
    print(run_length_encoding(sample_5))