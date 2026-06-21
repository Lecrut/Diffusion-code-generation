def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = data[i]
            count = 1
    encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "aaabbcdddd"
    result = run_length_encode(sample_input)
    print(result)
    sample_empty = ""
    print(run_length_encode(sample_empty))
    sample_single = "x"
    print(run_length_encode(sample_single))