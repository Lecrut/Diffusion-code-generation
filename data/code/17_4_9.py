def run_length_encode(s: str) -> str:
    if not s:
        return ""

    compressed = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1

    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == "__main__":
    sample1 = "aabccc"
    print(run_length_encode(sample1))

    sample2 = "aabbccc"
    print(run_length_encode(sample2))

    sample3 = "abc"
    print(run_length_encode(sample3))

    sample4 = ""
    print(run_length_encode(sample4))

    sample5 = "aaaaa"
    print(run_length_encode(sample5))