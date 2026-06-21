def rle_encode(s):
    if not s:
        return ""
    result = []
    n = len(s)
    i = 0
    while i < n:
        char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1
        if count > 9:
            full_blocks = count // 9
            remainder = count % 9
            for _ in range(full_blocks):
                result.append(f"{char}9")
            if remainder > 0:
                result.append(f"{char}{remainder}")
        else:
            result.append(f"{char}{count}")
        i = j
    return "".join(result)

if __name__ == '__main__':
    sample1 = "AAAABBBCC"
    sample2 = "AAAAAAABBBBCCCCC"
    sample3 = "AB"
    sample4 = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
    print(rle_encode(sample1))
    print(rle_encode(sample2))
    print(rle_encode(sample3))
    print(rle_encode(sample4))