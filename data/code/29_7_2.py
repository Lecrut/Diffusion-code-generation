def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDD"
    result = run_length_encode(sample_input)
    print(result)
    sample_input_2 = "AABBCCDD"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)
    sample_input_3 = "A"
    result_3 = run_length_encode(sample_input_3)
    print(result_3)
    sample_input_4 = ""
    result_4 = run_length_encode(sample_input_4)
    print(result_4)
    sample_input_5 = "Hello  World"
    result_5 = run_length_encode(sample_input_5)
    print(result_5)