def run_length_encode(binary_sequence: str) -> str:
    if not binary_sequence:
        return ""
    encoded = []
    current_char = binary_sequence[0]
    count = 1
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = binary_sequence[i]
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "1110000111110011111111"
    result = run_length_encode(sample_input)
    print(result)