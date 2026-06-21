def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    i = 1
    while i < len(s):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
        i += 1
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'AABBCC'
    encoded = run_length_encode(sample_input)
    print(encoded)