def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return "".join(compressed)

def solve(input_str):
    compressed = compress_string(input_str)
    if len(compressed) < len(input_str):
        return compressed
    return input_str

if __name__ == '__main__':
    result = solve("aabcccccaaa")
    print(result)