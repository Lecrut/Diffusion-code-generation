def run_length_encode(data):
    if not data:
        return ""
    result = []
    length = len(data)
    current_char = data[0]
    count = 1
    for i in range(1, length):
        if data[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = data[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccdddddeee"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)