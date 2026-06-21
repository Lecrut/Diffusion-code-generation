def run_length_encode(data: str) -> list:
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = data[i]
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)