def run_length_encode(s):
    if not s:
        return []
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    print(run_length_encode(sample_string))
    print(run_length_encode(""))
    print(run_length_encode("ABC"))
    print(run_length_encode("A"))