from typing import Optional

def compress_string(s: str) -> Optional[str]:
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    result = "".join(compressed)
    if len(result) < len(s):
        return result
    return None

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)