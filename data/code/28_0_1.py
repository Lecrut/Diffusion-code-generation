def run_length_encode(data):
    result = []
    current_char = None
    count = 0
    for char in data:
        if char == current_char:
            count += 1
        else:
            if current_char is not None:
                result.append([current_char, count])
            current_char = char
            count = 1
    if current_char is not None:
        result.append([current_char, count])
    return result

if __name__ == '__main__':
    sample_string = "aaabbc"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)