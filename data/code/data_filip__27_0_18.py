def run_length_encode(s: str) -> list:
    if not s:
        return []
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append((s[i - 1], count))
            count = 1
    encoded.append((s[-1], count))
    return encoded

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    result = run_length_encode(sample_input)
    print(result)