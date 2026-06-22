def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    current_char = data[0]
    for i in range(1, length):
        if data[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = data[i]
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)