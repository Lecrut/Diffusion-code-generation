def run_length_encode(strings):
    if not strings:
        return []
    encoded = []
    current_item = strings[0]
    count = 1
    for i in range(1, len(strings)):
        if strings[i] == current_item:
            count += 1
        else:
            encoded.append((count, current_item))
            current_item = strings[i]
            count = 1
    encoded.append((count, current_item))
    return encoded

if __name__ == '__main__':
    sample_data = ["a", "a", "b", "b", "b", "c", "a", "a", "a"]
    result = run_length_encode(sample_data)
    print(result)