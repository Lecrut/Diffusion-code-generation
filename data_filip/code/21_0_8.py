def run_length_encoding(data: str) -> list[tuple[str, int]]:
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for index in range(1, len(data)):
        if data[index] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[index]
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "aaabbccccdd"
    result = run_length_encoding(sample_string)
    print(result)