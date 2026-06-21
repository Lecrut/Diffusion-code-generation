def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

def solve(input_string: str) -> str:
    compressed = compress_string(input_string)
    if len(compressed) < len(input_string):
        return compressed
    return input_string

if __name__ == "__main__":
    sample_text = "aabcccccaaa"
    result = solve(sample_text)
    print(result)