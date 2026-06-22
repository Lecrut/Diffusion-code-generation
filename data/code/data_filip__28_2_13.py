def run_length_encode(s):
    if not s:
        return ""
    groups = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = char
            count = 1
    groups.append((current_char, count))
    return ''.join([f"{char}{count}" for char, count in groups])

if __name__ == '__main__':
    sample_string = "aaaabbbccddddde"
    print(run_length_encode(sample_string))