def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    print(run_length_encode(test_string))
    empty_string = ""
    print(run_length_encode(empty_string))
    single_char = "A"
    print(run_length_encode(single_char))
    mixed = "aaabbbaaccccc"
    print(run_length_encode(mixed))