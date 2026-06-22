def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    encoded = run_length_encode(sample_text)
    print(encoded)