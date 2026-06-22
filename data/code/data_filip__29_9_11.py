def encode_repeats(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    n = len(s)
    for i in range(n):
        if i + 1 < n and s[i] == s[i + 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{s[i]}")
            else:
                result.append(s[i])
            count = 1
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    print(encode_repeats(sample_input))