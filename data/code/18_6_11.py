def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccdd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)