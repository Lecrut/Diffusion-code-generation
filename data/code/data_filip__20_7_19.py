def run_length_encode(digit_sequence):
    if not digit_sequence:
        return ""
    encoded_parts = []
    current_char = digit_sequence[0]
    count = 1
    for i in range(1, len(digit_sequence)):
        if digit_sequence[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = digit_sequence[i]
            count = 1
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_sequence = "1112234444556667777788999"
    result = run_length_encode(sample_sequence)
    print(result)