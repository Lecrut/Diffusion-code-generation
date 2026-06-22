def run_length_encode(data):
    if not data:
        return []
    result = []
    current_item = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = data[i]
            count = 1
    result.append((current_item, count))
    return result

if __name__ == '__main__':
    sample_data = ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'E', 'E', 'E', 'E']
    encoded = run_length_encode(sample_data)
    print(encoded)