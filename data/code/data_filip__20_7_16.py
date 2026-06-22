def run_length_encode_digits(sequence: str) -> str:
    if not sequence:
        return ""
    encoded = []
    count = 1
    current_char = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = sequence[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_sequence = "11122233"
    print(run_length_encode_digits(sample_sequence))