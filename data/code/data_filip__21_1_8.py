def run_length_encode(data):
    if not data:
        return {}

    counts = {}
    current_char = data[0]
    current_count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            current_count += 1
        else:
            counts[current_char] = current_count
            current_char = data[i]
            current_count = 1

    counts[current_char] = current_count
    return counts

if __name__ == '__main__':
    sample1 = "AAABBBCCDAA"
    sample2 = "ABABABAB"
    sample3 = ""
    sample4 = "ZZZZZ"

    result1 = run_length_encode(sample1)
    result2 = run_length_encode(sample2)
    result3 = run_length_encode(sample3)
    result4 = run_length_encode(sample4)

    print(result1)
    print(result2)
    print(result3)
    print(result4)