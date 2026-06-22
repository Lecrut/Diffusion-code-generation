def compress_sequence(sequence):
    if not sequence:
        return ""
    result = []
    count = 1
    current_char = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = sequence[i]
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'wwwwaaadexxxxxx'
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)