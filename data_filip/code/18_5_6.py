def run_length_encode(data):
    if not data:
        return ""
    result = []
    chars = list(data)
    current_char = chars[0]
    count = 1
    for i in range(1, len(chars)):
        if chars[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = chars[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    test_cases = ["", "a", "aa", "aabbbcccc", "1112223"]
    for case in test_cases:
        encoded = run_length_encode(case)
        print(encoded)