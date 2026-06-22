def run_length_encoding(data):
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
    sample_input = "aaabbbccccdd"
    encoded_result = run_length_encoding(sample_input)
    print(encoded_result)
    empty_result = run_length_encoding("")
    print(empty_result)
    single_result = run_length_encoding("z")
    print(single_result)