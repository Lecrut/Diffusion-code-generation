def run_length_encode(items):
    if not items:
        return []
    encoded = []
    current_item = items[0]
    count = 1
    for i in range(1, len(items)):
        if items[i] == current_item:
            count += 1
        else:
            encoded.append((count, current_item))
            current_item = items[i]
            count = 1
    encoded.append((count, current_item))
    return encoded

if __name__ == '__main__':
    sample_data = ["apple", "apple", "banana", "banana", "banana", "cherry", "apple"]
    result = run_length_encode(sample_data)
    print(result)