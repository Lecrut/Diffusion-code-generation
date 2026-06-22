def run_length_encode(strings):
    if not strings:
        return []
    encoded = []
    current_value = strings[0]
    count = 1
    for i in range(1, len(strings)):
        if strings[i] == current_value:
            count += 1
        else:
            encoded.append((count, current_value))
            current_value = strings[i]
            count = 1
    encoded.append((count, current_value))
    return encoded

if __name__ == '__main__':
    sample_data = ["apple", "apple", "banana", "banana", "banana", "cherry", "apple"]
    result = run_length_encode(sample_data)
    print(result)