def encode_list(strings):
    if not strings:
        return []
    encoded = []
    current_char = strings[0]
    count = 1
    for i in range(1, len(strings)):
        if strings[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = strings[i]
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_data = ["apple", "apple", "banana", "banana", "banana", "cherry", "apple", "apple", "apple"]
    result = encode_list(sample_data)
    print(result)