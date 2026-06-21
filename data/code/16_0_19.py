def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)