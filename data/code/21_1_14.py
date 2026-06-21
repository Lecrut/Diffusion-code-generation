def run_length_encode(data):
    if not data:
        return {}
    counts = {}
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if current_char in counts:
                counts[current_char] += count
            else:
                counts[current_char] = count
            current_char = char
            count = 1
    if current_char in counts:
        counts[current_char] += count
    else:
        counts[current_char] = count
    return counts

if __name__ == '__main__':
    test_string = "AAABBBCCDAA"
    result = run_length_encode(test_string)
    print(result)
    test_string_2 = ""
    result_2 = run_length_encode(test_string_2)
    print(result_2)
    test_string_3 = "ZZZZZ"
    result_3 = run_length_encode(test_string_3)
    print(result_3)