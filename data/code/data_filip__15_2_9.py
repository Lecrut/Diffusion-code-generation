def compress_sequence(sequence):
    if not sequence:
        return ""
    result = []
    current_char = sequence[0]
    count = 1
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
    sample = 'wwwwaaadexxxxxx'
    print(compress_sequence(sample))