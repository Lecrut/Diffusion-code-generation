def run_length_encode_numeric_string(s):
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
    sample_string = "111223333444444"
    encoded = run_length_encode_numeric_string(sample_string)
    print(encoded)