def run_length_encoding(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_string = "aaabbccccdd"
    encoded_result = run_length_encoding(sample_string)
    print(encoded_result)