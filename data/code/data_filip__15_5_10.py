def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    current_char = s[0]
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
    sample_input = "cccccccccc"
    result = compress_string(sample_input)
    print(result)