def rle_compress_twist(s):
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
        if count >= 3:
            result.append(char)
            result.append(str(count))
        else:
            result.extend([char] * count)
        i += count
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbbcc"
    sample2 = "aabb"
    sample3 = "aaaabbbbccdd"
    sample4 = ""
    sample5 = "abc"
    sample6 = "aaabbbccc"
    
    print(rle_compress_twist(sample1))
    print(rle_compress_twist(sample2))
    print(rle_compress_twist(sample3))
    print(rle_compress_twist(sample4))
    print(rle_compress_twist(sample5))
    print(rle_compress_twist(sample6))