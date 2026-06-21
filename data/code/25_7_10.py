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
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

def is_compression_effective(s):
    encoded = run_length_encode(s)
    return len(encoded) < len(s)

if __name__ == '__main__':
    sample_strings = ["AAAABBBCCDAA", "ABCDE", "AABBCC", "AAAAA", "AB"]
    for s in sample_strings:
        result = is_compression_effective(s)
        print(result)