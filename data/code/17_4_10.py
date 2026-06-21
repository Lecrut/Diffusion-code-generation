def run_length_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    encoded = run_length_encode(sample_input)
    print(encoded)