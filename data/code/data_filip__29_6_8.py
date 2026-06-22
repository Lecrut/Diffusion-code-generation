def compress_string(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        count = 1
        while i + count < n and s[i + count] == char:
            count += 1
        result.append(f"{char}{count}")
        i += count
    return "".join(result)

if __name__ == '__main__':
    input_string = "aaabbc"
    compressed = compress_string(input_string)
    print(compressed)