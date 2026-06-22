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
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbc"
    print(run_length_encode(sample))
    sample2 = "hello"
    print(run_length_encode(sample2))
    sample3 = ""
    print(run_length_encode(sample3))
    sample4 = "a"
    print(run_length_encode(sample4))