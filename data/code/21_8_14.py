def run_length_encode(s: str) -> list[tuple[str, int]]:
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbbccdaaa"
    encoded = run_length_encode(sample_string)
    print(encoded)
    sample_string2 = "abc"
    encoded2 = run_length_encode(sample_string2)
    print(encoded2)
    sample_string3 = ""
    encoded3 = run_length_encode(sample_string3)
    print(encoded3)
    sample_string4 = "zzzzz"
    encoded4 = run_length_encode(sample_string4)
    print(encoded4)