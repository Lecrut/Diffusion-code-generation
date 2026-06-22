def run_length_compress(sequence):
    if not sequence:
        return ""

    compressed = []
    current_char = sequence[0]
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = sequence[i]
            count = 1

    compressed.append(current_char)
    compressed.append(str(count))

    return "".join(compressed)

if __name__ == '__main__':
    sample_sequence = 'wwwwaaadexxxxxx'
    result = run_length_compress(sample_sequence)
    print(result)