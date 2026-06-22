def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1])
            encoded.append(str(count))
            count = 1
    encoded.append(s[-1])
    encoded.append(str(count))
    return "".join(encoded)

def is_compression_effective(original_string):
    if not original_string:
        return False
    encoded = run_length_encode(original_string)
    return len(encoded) < len(original_string)

if __name__ == '__main__':
    sample_strings = ["AAABBBCCD", "ABCDEFG", "A", "AAAAAAA"]
    for s in sample_strings:
        encoded = run_length_encode(s)
        effective = is_compression_effective(s)
        print(f"Original: {s}, Encoded: {encoded}, Effective: {effective}")