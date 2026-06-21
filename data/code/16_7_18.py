def run_length_encode(binary_string):
    if not binary_string:
        return []
    counts = []
    current_char = binary_string[0]
    count = 1
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            counts.append(count)
            current_char = binary_string[i]
            count = 1
    counts.append(count)
    return counts

if __name__ == '__main__':
    sample_input = "1100011100"
    result = run_length_encode(sample_input)
    print(result)