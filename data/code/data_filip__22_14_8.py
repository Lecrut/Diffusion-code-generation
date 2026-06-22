def compress_string(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

def solve(s: str) -> str:
    compressed = compress_string(s)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == "__main__":
    sample_input = "aabcccccaaa"
    result = solve(sample_input)
    print(result)