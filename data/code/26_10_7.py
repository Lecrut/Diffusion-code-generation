def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1
        if count == 1:
            result.append(char)
        elif count == 2:
            result.append(char)
            result.append(char)
        else:
            result.append(f"{char}{count}")
        i = j
    return "".join(result)

if __name__ == "__main__":
    test_strings = [
        "AAABBBCCCC",
        "A",
        "AABBCC",
        "AAABBC",
        "ABBB",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "Hello World",
        "1112233334"
    ]
    for test in test_strings:
        print(f"{test} -> {rle_encode(test)}")