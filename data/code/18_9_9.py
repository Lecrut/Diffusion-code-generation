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
            result.append((count, current_char))
            current_char = s[i]
            count = 1
    result.append((count, current_char))
    return "".join(str(count) + char for count, char in result)

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    encoded = run_length_encode(sample)
    print(encoded)