def run_length_encode(s: str) -> str:
    if not s:
        return ""

    encoded = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1

    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    result1 = run_length_encode("AAABBBCCDAA")
    print(result1)

    result2 = run_length_encode("ABC")
    print(result2)

    result3 = run_length_encode("")
    print(result3)

    result4 = run_length_encode("A")
    print(result4)

    result5 = run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
    print(result5)