def run_length_encode_numeric(s):
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_string = "1122333444445"
    encoded = run_length_encode_numeric(sample_string)
    print(encoded)