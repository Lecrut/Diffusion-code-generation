def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCCDAA",
        "ABC",
        "AAAAAAAAA",
        "",
        "AABBCCDDAABB",
        "mississippi"
    ]
    for s in sample_strings:
        print(run_length_encode(s))