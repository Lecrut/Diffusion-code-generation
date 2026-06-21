def run_length_encode(strings):
    if not strings:
        return []
    result = []
    current = strings[0]
    count = 1
    for i in range(1, len(strings)):
        if strings[i] == current:
            count += 1
        else:
            result.append((count, current))
            current = strings[i]
            count = 1
    result.append((count, current))
    return result

if __name__ == '__main__':
    sample_data = ["apple", "apple", "banana", "banana", "banana", "cherry", "apple"]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)