def run_length_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1

    result.append(current_char)
    result.append(str(count))

    compressed = "".join(result)

    if len(compressed) < len(s):
        return compressed

    return s

if __name__ == '__main__':
    print(run_length_encode("aaabbcccc"))
    print(run_length_encode("abc"))
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aabbc"))