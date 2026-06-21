def run_length_encode(s):
    if not s:
        return {}

    filtered = [ch for ch in s if ch.isalnum()]

    if not filtered:
        return {}

    result = {}
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
    sample1 = "AAABBBCCD"
    sample2 = "AABBCCDD"
    sample3 = "HELLO WORLD"
    sample4 = ""
    sample5 = "A"

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))