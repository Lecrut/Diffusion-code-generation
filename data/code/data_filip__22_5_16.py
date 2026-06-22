def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_inputs = [
        "AAAABBBCCDAA",
        "ABC",
        "AABBCCDD",
        "AAAAA",
        "",
        "A"
    ]
    for sample in sample_inputs:
        print(run_length_encode(sample))