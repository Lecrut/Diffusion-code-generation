def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + s[i - 1])
            count = 1
    encoded.append(str(count) + s[-1])
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aaabb444cccd$$$$e1"
    result = run_length_encode(sample_input)
    print(result)