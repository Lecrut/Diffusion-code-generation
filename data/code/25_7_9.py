def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{s[i - 1]}{count}")
            count = 1
    encoded.append(f"{s[-1]}{count}")
    return "".join(encoded)

def is_compression_effective(original, compressed):
    return len(compressed) < len(original)

if __name__ == "__main__":
    sample_string = "AAABBBCCDDD"
    compressed_string = run_length_encode(sample_string)
    effective = is_compression_effective(sample_string, compressed_string)
    print(f"Original: {sample_string}, Length: {len(sample_string)}")
    print(f"Compressed: {compressed_string}, Length: {len(compressed_string)}")
    print(f"Compression Effective: {effective}")