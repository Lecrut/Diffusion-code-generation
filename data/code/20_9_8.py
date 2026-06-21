def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for item in data[1:]:
        if item == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = item
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)