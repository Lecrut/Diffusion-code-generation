def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aaabbcc111!!@#33"
    result = run_length_encode(sample_input)
    print(result)