def run_length_encode(s):
    filtered = [c for c in s if c.isalnum()]
    if not filtered:
        return {}
    result = {}
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
    sample_string = "aaabbcceee"
    print(run_length_encode(sample_string))
    sample_string2 = "AABBBCCCC"
    print(run_length_encode(sample_string2))
    sample_string3 = ""
    print(run_length_encode(sample_string3))
    sample_string4 = "a"
    print(run_length_encode(sample_string4))