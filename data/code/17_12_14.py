def run_length_encode(s):
    if not s:
        return {}
    result = {}
    filtered = [c for c in s if c.isalnum()]
    if not filtered:
        return {}
    current_char = filtered[0]
    count = 1
    for char in filtered[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_string = "aaabbcddddd11122!!abc"
    encoded = run_length_encode(sample_string)
    print(encoded)