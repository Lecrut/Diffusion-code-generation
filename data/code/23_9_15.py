def run_length_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        current_char = s[i]
        count = 1
        i += 1
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_value = run_length_encode(sample_input)
    print(encoded_value)