def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

def is_compression_effective(original):
    encoded = run_length_encode(original)
    return len(encoded) < len(original)

if __name__ == '__main__':
    sample1 = "aabbbcccc"
    sample2 = "abcdef"
    print(is_compression_effective(sample1))
    print(is_compression_effective(sample2))