def run_length_encode(sequence):
    if not sequence:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{sequence[i - 1]}")
            count = 1
    encoded.append(f"{count}{sequence[-1]}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    print(run_length_encode(sample_input))