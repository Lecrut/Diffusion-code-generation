def encode_run_length(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    char = s[0]

    for i in range(1, len(s)):
        current = s[i]
        if current == char:
            count += 1
        else:
            result.append(f"{count}{char}")
            char = current
            count = 1

    result.append(f"{count}{char}")
    return "".join(result)

if __name__ == "__main__":
    print(encode_run_length("aaabbcccc"))
    print(encode_run_length(""))
    print(encode_run_length("abc"))