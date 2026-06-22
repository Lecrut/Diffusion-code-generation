def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbc"
    print(run_length_encode(sample1))
    sample2 = "aabcccccaaa"
    print(run_length_encode(sample2))
    sample3 = ""
    print(run_length_encode(sample3))
    sample4 = "abcdefgh"
    print(run_length_encode(sample4))
    sample5 = "aaaaa"
    print(run_length_encode(sample5))
    sample6 = "a"
    print(run_length_encode(sample6))
    sample7 = "  "
    print(run_length_encode(sample7))
    sample8 = "!@#$%^^&*"
    print(run_length_encode(sample8))
    sample9 = "112233"
    print(run_length_encode(sample9))
    sample10 = "AABBCCDD"
    print(run_length_encode(sample10))