def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoded.append(str(count) + s[i])
        i += 1
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBCDD"
    result = run_length_encode(sample_string)
    print(result)