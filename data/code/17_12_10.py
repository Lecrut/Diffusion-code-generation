def run_length_encode(s):
    result = {}
    if not s:
        return result

    filtered = ''.join(c for c in s if c.isalnum())

    if not filtered:
        return result

    current_char = filtered[0]
    count = 1

    for i in range(1, len(filtered)):
        if filtered[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = filtered[i]
            count = 1

    result[current_char] = count
    return result

if __name__ == '__main__':
    sample = "aaabbcdeeee"
    encoded = run_length_encode(sample)
    print(encoded)