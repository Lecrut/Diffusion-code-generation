def encode_run_length(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccddde"
    encoded_result = encode_run_length(sample_input)
    print(encoded_result)