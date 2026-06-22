def run_length_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1

    result.append(current_char + str(count))

    compressed = "".join(result)
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == '__main__':
    sample_input = "aaabbbcc"
    output = run_length_encode(sample_input)
    print(output)