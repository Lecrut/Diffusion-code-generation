def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "1122233334455555"
    result = run_length_encode(sample_string)
    print(result)