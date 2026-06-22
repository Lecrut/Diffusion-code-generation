def run_length_encode(s):
    if not s:
        return {}
    filtered = [c for c in s if c.isalnum()]
    if not filtered:
        return {}
    result = {}
    current_char = filtered[0]
    count = 1
    for i in range(1, len(filtered)):
        if filtered[i] == current_char:
            count += 1
        else:
            key = current_char
            result[key] = count
            current_char = filtered[i]
            count = 1
    key = current_char
    result[key] = count
    return result

if __name__ == '__main__':
    sample_input = "aaabbcddddde"
    print(run_length_encode(sample_input))