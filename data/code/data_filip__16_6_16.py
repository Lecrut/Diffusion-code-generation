def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for item in data[1:]:
        if item == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = item
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_list = ["a", "a", "a", "b", "b", "c", "a", "a"]
    result = run_length_encode(sample_list)
    print(result)