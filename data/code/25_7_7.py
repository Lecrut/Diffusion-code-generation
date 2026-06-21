import re

def is_compression_effective(original: str) -> bool:
    if not original:
        return False
    encoded = run_length_encode(original)
    return len(encoded) < len(original)

def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "aaabbcccc"
    result1 = is_compression_effective(sample1)
    print(result1)

    sample2 = "abcdef"
    result2 = is_compression_effective(sample2)
    print(result2)

    sample3 = "aabbcc"
    result3 = is_compression_effective(sample3)
    print(result3)

    sample4 = "aaaaabbbbbccccc"
    result4 = is_compression_effective(sample4)
    print(result4)

    sample5 = ""
    result5 = is_compression_effective(sample5)
    print(result5)