def run_length_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    length = len(s)

    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1

    result.append(f"{count}{s[-1]}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbcccc"
    encoded_string = run_length_encode(sample_string)
    print(encoded_string)