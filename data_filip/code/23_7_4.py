def run_length_encode(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)