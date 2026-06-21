def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded_result = []
    current_char = data[0]
    count = 1
    for index in range(1, len(data)):
        if data[index] == current_char:
            count += 1
        else:
            encoded_result.append(f"{current_char}{count}")
            current_char = data[index]
            count = 1
    encoded_result.append(f"{current_char}{count}")
    return "".join(encoded_result)

if __name__ == '__main__':
    sample_input = 'AAAABBBCCDAA'
    print(run_length_encode(sample_input))