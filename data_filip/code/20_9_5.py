def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_value = data[0]
    current_count = 1
    for item in data[1:]:
        if item == current_value:
            current_count += 1
        else:
            encoded.append((current_count, current_value))
            current_value = item
            current_count = 1
    encoded.append((current_count, current_value))
    return encoded

if __name__ == '__main__':
    sample_list = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a']
    result = run_length_encode(sample_list)
    print(result)