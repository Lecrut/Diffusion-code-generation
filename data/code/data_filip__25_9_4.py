def run_length_encode(s):
    if not s:
        return ""

    result_parts = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result_parts.append(str(count) + current_char)
            current_char = s[i]
            count = 1

    result_parts.append(str(count) + current_char)

    return "".join(result_parts)

if __name__ == '__main__':
    sample_string = "aaaabbbcccd"
    encoded = run_length_encode(sample_string)
    print(encoded)

    sample_string2 = "aabb"
    encoded2 = run_length_encode(sample_string2)
    print(encoded2)

    sample_string3 = ""
    encoded3 = run_length_encode(sample_string3)
    print(encoded3)

    sample_string4 = "abcdef"
    encoded4 = run_length_encode(sample_string4)
    print(encoded4)

    sample_string5 = "aaabbaaa"
    encoded5 = run_length_encode(sample_string5)
    print(encoded5)