def run_length_encode(sequence):
    if not sequence:
        return {}
    result = {}
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample = "aaabbcdd"
    print(run_length_encode(sample))