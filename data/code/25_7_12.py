def compress(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            result.append(str(count))
            count = 1
    result.append(s[-1])
    result.append(str(count))
    return "".join(result)

def check_compression_efficiency(original, encoded):
    if not encoded:
        return False
    original_len = len(original)
    encoded_len = len(encoded)
    return original_len > encoded_len

def evaluate(original_str):
    rle = compress(original_str)
    is_efficient = check_compression_efficiency(original_str, rle)
    original_length = len(original_str)
    rle_length = len(rle)
    return {
        "original": original_str,
        "rle": rle,
        "original_length": original_length,
        "rle_length": rle_length,
        "is_efficient": is_efficient
    }

if __name__ == '__main__':
    test_string = "aabcccccaaa"
    result = evaluate(test_string)
    print(result)