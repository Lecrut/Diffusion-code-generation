def run_length_encode(sequence):
    if not sequence:
        return {}

    counts = {}
    current_char = sequence[0]
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            counts[current_char] = count
            current_char = sequence[i]
            count = 1

    counts[current_char] = count
    return counts

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)

    sample_input2 = "hello"
    result2 = run_length_encode(sample_input2)
    print(result2)

    sample_input3 = "aabbbcccc"
    result3 = run_length_encode(sample_input3)
    print(result3)

    sample_input4 = ""
    result4 = run_length_encode(sample_input4)
    print(result4)

    sample_input5 = "xyz"
    result5 = run_length_encode(sample_input5)
    print(result5)