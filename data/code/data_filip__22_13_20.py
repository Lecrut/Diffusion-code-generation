def rle_compress(s: str) -> str:
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        current_char = s[i]
        count = 1
        while i + count < n and s[i + count] == current_char:
            count += 1
        if count >= 3:
            result.append(f"{current_char}{count}")
        else:
            result.append(current_char * count)
        i += count
    return "".join(result)

if __name__ == "__main__":
    test_input = "aaabbcdddddeefff"
    compressed = rle_compress(test_input)
    print(compressed)