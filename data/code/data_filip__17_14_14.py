def run_length_encode(s):
    if not s:
        return ""
    encoded = ""
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded += str(count) + current_char
            current_char = s[i]
            count = 1
    encoded += str(count) + current_char
    return encoded

if __name__ == '__main__':
    sample_string = "AAABBBCCCDAA"
    result = run_length_encode(sample_string)
    print(result)