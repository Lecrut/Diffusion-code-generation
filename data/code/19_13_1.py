def run_length_encode(sequence):
    if not sequence:
        return ""

    encoded = []
    current_char = sequence[0]
    count = 1

    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1

    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_sequences = [
        "AAABBBCCD",
        "A",
        "ABABAB",
        "AAAAA",
        "XYZ",
        ""
    ]

    for seq in sample_sequences:
        result = run_length_encode(seq)
        print(result)