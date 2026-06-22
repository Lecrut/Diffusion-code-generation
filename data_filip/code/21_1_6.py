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
            counts[current_char] = count
            current_char = char
            count = 1
    counts[current_char] = count
    return counts

if __name__ == '__main__':
    sample_inputs = [
        "aaabbc",
        "hello",
        "aabbbccccd",
        "single",
        "aa"
    ]
    for sample in sample_inputs:
        result = run_length_encode(sample)
        print(f"Input: {sample}, Output: {result}")