def rle_compress(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    n = len(s)
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

if __name__ == "__main__":
    test_cases = ["", "a", "aa", "aabcccccaaa", "abbbcccd"]
    for case in test_cases:
        result = rle_compress(case)
        print(result)