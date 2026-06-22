def run_length_encode(s: str) -> list:
    result = []
    if not s:
        return result
    count = 1
    char = s[0]
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            result.append((char, count))
            char = s[i]
            count = 1
    result.append((char, count))
    return result

if __name__ == '__main__':
    sample_text = "aaabbbccccc"
    encoded = run_length_encode(sample_text)
    print(encoded)