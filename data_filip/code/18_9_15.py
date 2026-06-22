def run_length_encode(data):
    if not data:
        return []
    result = []
    length = len(data)
    i = 0
    while i < length:
        current_char = data[i]
        count = 1
        while i + count < length and data[i + count] == current_char:
            count += 1
        result.append((current_char, count))
        i += count
    return result

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)