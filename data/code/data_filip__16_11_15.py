def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbbccccddeee"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)